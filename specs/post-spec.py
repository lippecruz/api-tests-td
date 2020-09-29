import requests
import json
import re

from helpers import helper

# Test Payloads
payload = {'ID': 10000, 'Title': 'Activity Test', 'DueDate': '2020-12-30T08:18:32.9456988+00:00'}
invalid_id_payload = {'ID': 'aa', 'Title': 'Activity aa', 'DueDate': '2020-12-30T08:18:32.9456988+00:00'}
no_due_date_payload = {'ID': 1000, 'Title': 'Activity aa'}


def test_post_activity():
    response = requests.post(helper.base_url, data=json.dumps(payload), headers=helper.headers)
    activity = response.json()

    assert response.status_code == 200

    assert activity["ID"] == 10000
    assert activity["Title"] == 'Activity Test'
    assert activity["DueDate"] == '2020-12-30T08:18:32.9456988+00:00'
    assert activity["Completed"] == False

def test_post_activity_invalid_id():
    response = requests.post(helper.base_url, data=json.dumps(invalid_id_payload), headers=helper.headers)
    activity = response.json()
 
    assert response.status_code == 200

    assert activity["ID"] == 0  # Default value
    assert activity["Title"] == 'Activity aa'
    assert activity["DueDate"] == '2020-12-30T08:18:32.9456988+00:00'
    assert activity["Completed"] == False  # Default value

def test_post_activity_without_due_date():
    response = requests.post(helper.base_url, data=json.dumps(no_due_date_payload), headers=helper.headers)
    activity = response.json()
 
    assert response.status_code == 200

    assert activity["ID"] == 1000
    assert activity["Title"] == 'Activity aa'
    assert activity["DueDate"] == '0001-01-01T00:00:00' # Default value
    assert activity["Completed"] == False  # Default value