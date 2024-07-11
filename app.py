# file: HealthWatch/app.py

import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.utils import secure_filename
from mock_fitbit_data import mock_data
from fitbit_api import fetch_fitbit_data

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'username' in session:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        profile_picture = 'static/images/profile_mockup.jpg'
        bio = request.form.get('bio', '')

        try:
            # Check if the username or email is already taken
            # For demo purposes, we skip actual database checks
            session['username'] = username
            session['email'] = email
            session['bio'] = bio
            session['profile_picture'] = profile_picture
            flash('User successfully registered!')
            return redirect(url_for('login'))

        except Exception as e:
            print(f"Error during registration: {e}")
            flash('An error occurred during registration. Please try again.')
            return redirect(url_for('register'))

    return render_template('register.html')

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # For demo purposes, we skip actual authentication
        if username == session.get('username'):
            session['username'] = username
            return redirect(url_for('dashboard'))
        flash('Invalid username or password!')
    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'username' not in session:
        flash('You are not logged in. Please log in to continue.')
        return redirect(url_for('login'))

    user = {
        'username': session.get('username'),
        'email': session.get('email'),
        'bio': session.get('bio'),
        'profile_picture': session.get('profile_picture'),
        'daily_steps': fetch_fitbit_data('daily_steps'),
        'heart_rate': fetch_fitbit_data('heart_rate'),
        'sleep_pattern': fetch_fitbit_data('sleep_pattern')
    }

    if request.method == 'POST':
        user['email'] = request.form['email']
        user['bio'] = request.form['bio']
        if 'password' in request.form and request.form['password']:
            # Update password (omitted for demo purposes)
            pass

        if 'profile_picture' in request.files:
            file = request.files['profile_picture']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                user['profile_picture'] = file_path

        session['email'] = user['email']
        session['bio'] = user['bio']
        session['profile_picture'] = user['profile_picture']
        flash('Profile updated successfully!')
        return redirect(url_for('dashboard'))

    return render_template('dashboard.html', user=user)

@app.route('/health_recommendations')
def health_recommendations():
    if 'username' not in session:
        return redirect(url_for('login'))
    recommendations = mock_data.get('health_recommendations', [])
    return render_template('health_recommendations.html', recommendations=recommendations)

@app.route('/historical_data')
def historical_data():
    if 'username' not in session:
        return redirect(url_for('login'))
    data = mock_data.get('historical_data', [])
    return render_template('historical_data.html', historical_data=data)

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
