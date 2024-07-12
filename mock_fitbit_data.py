# File: HealthWatch/mock_fitbit_data.py

""" bio sample : 
Tech explorer by day, fitness enthusiast by night. Coding my way through life's algorithms while chasing that runner's high. Always in beta, constantly upgrading. My commit history is as consistent as my workout streaks. Debugging both software and fitness goals, one step at a time. Fueled by curiosity, caffeine, and the occasional protein shake. Building a healthier version of myself, one line of code and one rep at a time. Welcome to my journey of bits, bytes, and burpees!

"""
import random
from datetime import datetime, timedelta

def generate_recommendations(weeks=12):
    recommendations = []
    activities = ["walking", "running", "cycling", "swimming", "yoga", "strength training"]
    nutrition_tips = ["Increase protein intake", "Add more vegetables to your diet", "Stay hydrated", "Reduce sugar consumption", "Eat more whole grains", "Include healthy fats in your meals"]
    sleep_tips = ["Maintain a consistent sleep schedule", "Create a relaxing bedtime routine", "Avoid screens before bed", "Keep your bedroom cool and dark", "Limit caffeine intake in the afternoon"]

    start_date = datetime.now() - timedelta(weeks=weeks)
    start_date = start_date - timedelta(days=start_date.weekday())  # Adjust to start on a Monday

    for week in range(1, weeks + 1):
        week_start = start_date + timedelta(weeks=week-1)
        week_end = week_start + timedelta(days=6)
        
        weekly_rec = {
            "week": week,
            "start_date": week_start.strftime('%Y-%m-%d'),
            "end_date": week_end.strftime('%Y-%m-%d'),
            "focus_area": random.choice(["Fitness", "Nutrition", "Sleep"]),
            "daily_recommendations": {}
        }

        for day in range(7):
            current_date = week_start + timedelta(days=day)
            if weekly_rec["focus_area"] == "Fitness":
                activity = random.choice(activities)
                duration = random.randint(20, 60)
                rec = f"{activity.capitalize()} for {duration} minutes"
            elif weekly_rec["focus_area"] == "Nutrition":
                rec = random.choice(nutrition_tips)
            else:  # Sleep
                rec = random.choice(sleep_tips)

            weekly_rec["daily_recommendations"][current_date.strftime('%Y-%m-%d')] = rec

        recommendations.append(weekly_rec)

    return recommendations

def generate_mock_data(days=30):
    mock_data = []
    start_date = datetime.now() - timedelta(days=days)
    for i in range(days):
        date = (start_date + timedelta(days=i)).strftime('%Y-%m-%d')
        steps = random.randint(2000, 10000)
        calories_burned = random.randint(1500, 3000)
        active_minutes = random.randint(30, 120)
        mock_data.append({
            "date": date,
            "steps": steps,
            "calories_burned": calories_burned,
            "active_minutes": active_minutes
        })
    return mock_data

historical_data = generate_mock_data(30)

mock_data = {
    "daily_steps": historical_data,
    "health_recommendations": generate_recommendations(12),  # 3 months (12 weeks)
    "heart_rate": {
        "date": datetime.now().strftime('%Y-%m-%d'),
        "value": random.randint(60, 80),
        "zones": [
            {"name": "Out of Range", "minutes": random.randint(150, 250)},
            {"name": "Fat Burn", "minutes": random.randint(30, 70)},
            {"name": "Cardio", "minutes": random.randint(10, 30)},
            {"name": "Peak", "minutes": random.randint(5, 15)}
        ]
    },
    "sleep_pattern": {
        "date": datetime.now().strftime('%Y-%m-%d'),
        "duration": random.randint(360, 540),
        "efficiency": random.randint(80, 95),
        "stages": {
            "light": random.randint(40, 70),
            "deep": random.randint(10, 30),
            "rem": random.randint(10, 25),
            "awake": random.randint(1, 10)
        }
    },
    "historical_data": historical_data,
    "user_profile": {
        "username": "johndoe",
        "email": "johndoe@example.com",
        "profile_picture": "images/profile_mockup.jpg",
        "joined_date": "2022-01-15",
        "bio": "Avid runner and tech enthusiast. Love to explore new technologies and innovations.",
        "daily_steps": f"{historical_data[-1]['steps']} steps on {historical_data[-1]['date']}",
        "heart_rate": f"Average heart rate of {random.randint(60, 80)} bpm on {datetime.now().strftime('%Y-%m-%d')}",
        "sleep_pattern": f"{random.randint(360, 540)} minutes of sleep with {random.randint(80, 95)}% efficiency on {datetime.now().strftime('%Y-%m-%d')}"
    }
}

def fetch_fitbit_data(data_type):
    # Simulate API call and fallback to mock data
    if random.choice([True, False]):  # Randomly decide to use mock data
        return mock_data.get(data_type)
    else:
        # Here, you would normally make an API call to Fitbit
        # For demo purposes, we'll use mock data
        return mock_data.get(data_type)