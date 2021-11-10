import requests

import json

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "-F0oHNJ9jo9hYnF5fznLzlYSp8TLCaUgnESEjYJPvtTL"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": ['Time',	'ActivePower(kW)',	'WindSpeed(m/s)',	'Theoretical_Power_Curve (KWh)',	'Wind_Direction'], "values": [416.328907824861, 5.31133604049682]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/d04dc6af-c706-4e1b-b17c-fb31a9094707/predictions?version=2021-10-29', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())
#print(predict([[416.328907824861,5.31133604049682]])[0],"KWh")