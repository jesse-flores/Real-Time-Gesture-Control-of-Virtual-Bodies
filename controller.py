import requests
import time

FLASK_URL = "http://localhost:5000/update_state"

##Sending input values

def send_state_to_flask(state):
    response = requests.post(FLASK_URL, json=state)
    if response.status_code == 200:
        print("Updated state")
    else:
        print("Failed to update state:", response.status_code)

while True:
    state = input_State() ##Needs updating
    send_state_to_flask(state)
    time.sleep(1)  ##Second updates