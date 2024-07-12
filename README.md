# HealthWatch - API Fitbit Tracker / Personal Trainer

HealthWatch is a comprehensive personal health monitoring application designed for individuals with chronic conditions, health enthusiasts, and seniors who require regular health tracking. It leverages the power of Fitbit API integration to provide real-time data tracking and personalized health recommendations.

## Key Features

- Real-time health data tracking using Fitbit API integration
- Personalized health dashboard with 90-day activity insights
- Customized health recommendations based on user data
- Historical data analysis and visualization
- User authentication and profile management

## Tech Stack

- Backend: Flask, SQLite
- Frontend: HTML, CSS, JavaScript, Chart.js
- APIs: Fitbit API (simulated in this version)
- Database: SQLAlchemy
- Authentication: Flask-Login



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

## Usage

1. Register for a new account or log in with existing credentials.
2. Connect your Fitbit account (simulated in this version).
3. View your personalized health dashboard with 90-day activity data.
4. Explore the interactive graph with zoom and pan capabilities.
5. Check your health recommendations and historical data analysis.
6. Update your profile information as needed.

## Project Structure

The application is organized as follows:

```plaintext
/project_root
|-- flask_app.py                        # Main Flask application
|-- /templates                          # HTML templates for Flask
|   |-- base.html                       # Base layout template
|   |-- dashboard.html                  # User dashboard
|   |-- health_recommendations.html     # Health recommendations page
|   |-- historical_data.html            # Historical data page
|   |-- login.html                      # Login page
|   |-- register.html                   # Registration page
|-- /static                             # Static files for Flask like CSS, JS
|   |-- styles.css                      # CSS styles
|   |-- app.js                          # JavaScript functions
|   |--/uploads                         # User profile pictures
|-- requirements.txt                    # Python dependencies
```
## Requirements

```txt
Flask==2.0.2
Flask-SQLAlchemy==2.5.1
SQLAlchemy==1.4.22
Werkzeug==2.0.2
Flask-Migrate==3.1.0
python-dotenv==0.19.1
pytest==6.2.5
gunicorn==20.1.0
```

## Key Components

- `app.py`: Main Flask application file
- `mock_fitbit_data.py`: Generates mock Fitbit data for demonstration
- `static/styles.css`: Custom CSS styles
- `static/app.js`: Custom JavaScript for interactive features
- `templates/`: HTML templates for the application

## Testing
- We use pytest for unit testing and GitHub Actions for continuous integration.
- Tests are located in the `tests/` directory and can be run using:
    ```sh
    pytest
    ```
- GitHub Actions will automatically run tests on every push and pull request to the main branch.

## Contributing

We welcome contributions to HealthWatch! Please read our contributing guidelines before submitting pull requests.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- Flask: Web framework for Python
- Chart.js: JavaScript charting library
- Bootstrap: Frontend component library

## Milestones
1. **Initial Setup and API Integration**
    - [x] Initialize the Flask project
    - [x] Set up SQLite database
    - [x] Integrate with Fitbit API
    - [x] User authentication and profile management

2. **Frontend Development**
    - [x] Set up Flask, html, css,javascript for the frontend
    - [x] Develop the health dashboard
    - [x] Profile management interface
    - [x] Health data visualization

3. **Testing and Deployment**
    - [x] Write unit tests for backend and frontend
    - [x] Set up GitHub Actions for CI/CD
    - [ ] Deploy the application on PythonAnywhere


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


