from HealthWatch.mock_fitbit_data import generate_mock_data, generate_recommendations
from datetime import datetime, timedelta

def test_generate_mock_data():
    data = generate_mock_data(days=30)
    assert len(data) == 30
    for entry in data:
        assert 'date' in entry
        assert 'steps' in entry
        assert 'calories_burned' in entry
        assert 'active_minutes' in entry
        assert 2000 <= entry['steps'] <= 10000
        assert 1500 <= entry['calories_burned'] <= 3000
        assert 30 <= entry['active_minutes'] <= 120

def test_generate_recommendations():
    recommendations = generate_recommendations(weeks=12)
    assert len(recommendations) == 12
    for week in recommendations:
        assert 'week' in week
        assert 'start_date' in week
        assert 'end_date' in week
        assert 'focus_area' in week
        assert 'daily_recommendations' in week
        assert len(week['daily_recommendations']) == 7