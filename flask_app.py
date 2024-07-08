from flask import Flask, jsonify
from mock_fitbit_data import mock_data

app = Flask(__name__)

@app.route('/api/fitbit/daily_steps')
def get_daily_steps():
    # This endpoint simulates fetching daily step count from Fitbit
    return jsonify(mock_data['daily_steps'])

@app.route('/api/fitbit/heart_rate')
def get_heart_rate():
    # This endpoint simulates fetching heart rate data from Fitbit
    return jsonify(mock_data['heart_rate'])

@app.route('/api/fitbit/sleep_pattern')
def get_sleep_pattern():
    # This endpoint simulates fetching sleep pattern data from Fitbit
    return jsonify(mock_data['sleep_pattern'])

if __name__ == '__main__':
    app.run(debug=True)
