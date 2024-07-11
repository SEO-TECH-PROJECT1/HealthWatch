# File: File: HealthWatch/mock_fitbit_data.py
# Example mock data mimicking Fitbit API responses for different metrics and user profile

mock_data = {
    "daily_steps": {
        "date": "2024-07-10",
        "steps": 7642
    },
    "heart_rate": {
        "date": "2024-07-10",
        "value": 72,  # Average beats per minute
        "zones": [
            {"name": "Out of Range", "minutes": 200},
            {"name": "Fat Burn", "minutes": 50},
            {"name": "Cardio", "minutes": 20},
            {"name": "Peak", "minutes": 10}
        ]
    },
    "sleep_pattern": {
        "date": "2024-07-10",
        "duration": 480,  # Duration in minutes
        "efficiency": 90,
        "stages": {
            "light": 60,
            "deep": 20,
            "rem": 15,
            "awake": 5
        }
    },
    "health_recommendations": [
        "Eat more greens and fruits for better vitamin intake.",
        "Consider increasing your water intake to 8 glasses per day.",
        "Regular exercise can help improve your heart health."
    ],
    "historical_data": [
        {"date": "2024-07-01", "steps": 5000, "calories_burned": 250},
        {"date": "2024-07-02", "steps": 7000, "calories_burned": 350},
        {"date": "2024-07-03", "steps": 4500, "calories_burned": 225}
    ],
    "user_profile": {
        "username": "johndoe",
        "email": "johndoe@example.com",
        "profile_picture": "static/images/profile_mockup.jpg",  # Assume profile picture is stored in static/images
        "joined_date": "2022-01-15",
        "bio": "Avid runner and tech enthusiast. Love to explore new technologies and innovations.",
        "daily_steps": "7642 steps on 2024-07-10",
        "heart_rate": "Average heart rate of 72 bpm on 2024-07-10",
        "sleep_pattern": "480 minutes of sleep with 90% efficiency on 2024-07-10"
    }
}
