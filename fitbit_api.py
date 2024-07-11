import requests
import hashlib
import base64
import random
import string
from pprint import pprint

class FitbitAPI:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def authorize(self, code_challenge, state):
        url = f"https://www.fitbit.com/oauth2/authorize?response_type=code&client_id={self.client_id}&scope=activity+cardio_fitness+electrocardiogram+heartrate+location+nutrition+oxygen_saturation+profile+respiratory_rate+settings+sleep+social+temperature+weight&code_challenge={code_challenge}&code_challenge_method=S256&state={state}"
        response = requests.get(url)
        return response.url


    def get_tokens(self, code, code_verifier):
        url = "https://api.fitbit.com/oauth2/token"
        headers = {
            "Authorization": f"Basic {base64.b64encode((self.client_id + ':' + self.client_secret).encode()).decode()}",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {
            "clientId": self.client_id,
            "grant_type": "authorization_code",
            "code": code,
            "code_verifier": code_verifier
        }
        response = requests.post(url, headers=headers, data=data)
        res_data = response.json()
        return res_data

    def get_profile(self, access_token):
        url = "https://api.fitbit.com/1/user/-/profile.json"
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        response = requests.get(url, headers=headers)
        return response.json()

    def get_weight(self, access_token):
        url = "https://api.fitbit.com/1/user/-/body/log/weight/date/today/1m.json"
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        response = requests.get(url, headers=headers)
        return response.json()

    def get_heartrate_timeseries(self, access_token):
        url = "https://api.fitbit.com/1/user/-/activities/heart/date/today/7d/1min.json"
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        response = requests.get(url, headers=headers)
        return response.json()

    def get_sleep(self, access_token):
        url = "https://api.fitbit.com/1.2/user/-/sleep/date/today.json"
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        response = requests.get(url, headers=headers)
        return response.json()

    def get_steps(self, access_token):
        url = "https://api.fitbit.com/1/user/-/activities/steps/date/today/1d.json"
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        response = requests.get(url, headers=headers)
        return response.json()

    def PCKE_generator(self):
        code_verifier = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=43))
        code_challenge = hashlib.sha256(code_verifier.encode()).digest()
        code_challenge = base64.urlsafe_b64encode(code_challenge).decode().strip('=')
        return code_verifier, code_challenge

    def generate_random_value(self, length):
        characters = string.ascii_lowercase + string.digits
        random_value = ''.join(random.choices(characters, k=length))
        return random_value

# Example usage:
CLIENT_ID = "23PFP8"
CLIENT_SECRET = "c6964127ec034058e8ccc4b33cf0cad9"

FAPI = FitbitAPI(CLIENT_ID, CLIENT_SECRET)
code_verifier, code_challenge = FAPI.PCKE_generator()
state = FAPI.generate_random_value(32)
link = FAPI.authorize(code_challenge, state)


# #redirects to localhost:5000/dashboard?

# #Flask app

# from flask import Flask, render_template, request, redirect, url_for, session, flash

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return redirect(link)
    

# @app.route('/dashboard')
# def dashboard():
#     code = request.args.get('code')
#     if code:
#         tokens = FAPI.get_tokens(code, code_verifier)
#         access_token = tokens['access_token']
#         profile = FAPI.get_profile(access_token)
#         return profile


# if __name__ == '__main__':
#     app.run()





