# HealthWatch - API Fitbit Tracker / Personal Trainer

HealthWatch is a personal health monitoring app designed for individuals with chronic conditions, health enthusiasts, and seniors needing regular health tracking. It integrates with the Fitbit API to provide real-time data tracking and personalized recommendations.

## Features
- Real-time health tracking using Fitbit API
- Personal health dashboard with insights
- Personalized health recommendations
- Historical data analysis
- User authentication and profile management

## Tech Stack
- **Backend**: Flask, SQLite
- **Frontend**: Streamlit
- **APIs**: Fitbit API, ChatGPT API
- **Deployment**: PythonAnywhere
- **Testing**: GitHub Actions



## Installation
1. Clone the repository
    ```sh
    git clone  https://github.com/SEO-TECH-PROJECT1/PROJECT_2_HealthWatch.git
    cd HealthWatch
    ```

2. Create and activate a virtual environment
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies
    ```sh
    pip install -r requirements.txt
    ```

4. Set up environment variables
    ```sh
    cp .env.example .env
    # Edit .env to include your Fitbit API credentials and other settings
    ```

5. Initialize the database
    ```sh
    flask db init
    flask db migrate
    flask db upgrade
    ```

6. Run the app
    ```sh
    flask run
    ```

## Deployment
- The application will be deployed on PythonAnywhere.
- Configure your PythonAnywhere environment to use Flask and set up the required environment variables.

## Testing
- We use GitHub Actions for continuous integration and testing.
- Tests are located in the `tests/` directory and can be run using:
    ```sh
    pytest tests/
    ```

## Milestones
1. **Initial Setup and API Integration**
    - [ ] Initialize the Flask project
    - [ ] Set up SQLite database
    - [ ] Integrate with Fitbit API
    - [ ] User authentication and profile management

2. **Frontend Development**
    - [ ] Set up Streamlit for the frontend
    - [ ] Develop the health dashboard
    - [ ] Profile management interface
    - [ ] Health data visualization

3. **Testing and Deployment**
    - [ ] Write unit tests for backend and frontend
    - [ ] Set up GitHub Actions for CI/CD
    - [ ] Deploy the application on PythonAnywhere

4. **Feedback and Iteration**
    - [ ] Collect user feedback
    - [ ] Implement improvements based on feedback

## Issues to Create on GitHub
1. **Setup Project Structure**
    - Set up Flask project
    - Initialize SQLite database
    - Set up basic routes and models

2. **Fitbit API Integration**
    - Create module for Fitbit API interaction
    - Implement data fetching and processing

3. **User Authentication**
    - Implement user login and registration
    - Set up user profile management

4. **Streamlit Frontend**
    - Develop health dashboard
    - Implement profile management interface
    - Visualize health data

5. **Testing**
    - Write unit tests for Fitbit API integration
    - Write unit tests for user management
    - Write unit tests for Flask routes

6. **Deployment**
    - Set up PythonAnywhere environment
    - Configure deployment settings
    - Automate deployment with GitHub Actions

7. **Feedback Collection**
    - Set up user feedback mechanism
    - Analyze feedback and prioritize improvements

## Project Structure

The application is organized as follows:

```plaintext
/project_root
|-- flask_app.py        # Main Flask application
|-- /templates          # HTML templates for Flask
|   |-- base.html       # Base layout template
|   |-- index.html      # Home page with login or registration option
|   |-- dashboard.html  # User dashboard
|   |-- health.html     # Health recommendations page
|   |-- history.html    # Historical data analysis page
|-- /static             # Static files for Flask like CSS, JS
|   |-- styles.css      # CSS styles
|   |-- app.js          # JavaScript functions
|-- requirements.txt    # Python dependencies



## Key Components

- **Flask**: The core framework used to create the web application.
- **Flask-SQLAlchemy**: An extension for Flask that adds support for SQLAlchemy, useful for handling database operations.
- **Werkzeug**: A comprehensive WSGI web application library, typically installed with Flask.
- **gunicorn**: A Python WSGI HTTP Server for UNIX, providing a powerful interface for deploying Flask applications in production environments. It's not necessary for local development but recommended for production setups.

## Installation

To set up the project environment and install the necessary Python packages, run the following command:

```bash
pip install -r requirements.txt




## Requirements

```txt
Flask==2.0.1
SQLAlchemy==1.4.22
Flask-Migrate==3.0.0
Streamlit==0.85.0
requests==2.25.1
pytest==6.2.4
python-dotenv==0.18.0
