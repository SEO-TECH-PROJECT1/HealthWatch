import streamlit as st
import requests

def fetch_fitbit_data(endpoint):
    """Fetch data from Flask which in turn gives mocked Fitbit data."""
    response = requests.get(f'http://localhost:5000/api/fitbit/{endpoint}')
    if response.status_code == 200:
        return response.json()
    else:
        st.error('Failed to retrieve data')

def main():
    st.title('HealthWatch Dashboard')
    if st.button('Get Daily Steps'):
        daily_steps = fetch_fitbit_data('daily_steps')
        st.write(daily_steps)

    if st.button('Get Heart Rate'):
        heart_rate = fetch_fitbit_data('heart_rate')
        st.write(heart_rate)

    if st.button('Get Sleep Pattern'):
        sleep_pattern = fetch_fitbit_data('sleep_pattern')
        st.write(sleep_pattern)

if __name__ == '__main__':
    main()
