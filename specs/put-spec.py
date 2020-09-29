import requests
import json
import re

from helpers import helper

# Test Payloads
payload = {'ID': 1, 'Title': 'Activity 1 Updated', 'DueDate': '2020-12-30T08:18:32.9456988+00:00', 'Completed': True}

def test_put_activity():
    response = requests.put(helper.base_url + "/1", data=json.dumps(payload), headers=helper.headers)
    activity = response.json()

    assert response.status_code == 200

    assert activity["ID"] == 1
    assert activity["Title"] == 'Activity 1 Updated'
    assert activity["DueDate"] == '2020-12-30T08:18:32.9456988+00:00'
    assert activity["Completed"] == True

def test_put_activity_invalid_id_status_code_equals_400():
    response = requests.put(helper.base_url  + "/a", data=json.dumps(payload), headers=helper.headers)
    activity = response.json()
 
    assert response.status_code == 400