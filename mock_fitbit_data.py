# Example mock data mimicking Fitbit API responses for different metrics

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
    }
}
