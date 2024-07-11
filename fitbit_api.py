import random
from mock_fitbit_data import mock_data

def fetch_fitbit_data(data_type):
    # Simulate API call and fallback to mock data
    if random.choice([True, False]):  # Randomly decide to use mock data
        return mock_data.get(data_type)
    else:
        # Here, you would normally make an API call to Fitbit
        # For demo purposes, we'll use mock data
        return mock_data.get(data_type)
