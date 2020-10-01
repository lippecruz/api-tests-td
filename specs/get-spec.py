import requests
import re

from helpers import helper

def test_get_activities_status_code_equals_200():
     response = requests.get(helper.base_url)
     assert response.status_code == 200

def test_get_activities_content_type_equals_json():
     response = requests.get(helper.base_url)
     result = "application/json; charset=utf-8"

     assert response.headers["Content-Type"] == result

def test_get_activities_length():
     response = requests.get(helper.base_url)
     response_body_length = len(response.json())

     assert response_body_length == 30

def test_get_activities_attributes():
     response = requests.get(helper.base_url)
     first_activity = response.json()[0]

     assert first_activity["ID"] == 1
     assert first_activity["Title"] == 'Activity 1'
     assert re.match(helper.pattern_date_time, first_activity["DueDate"])
     assert first_activity["Completed"] == False

def test_get_activity_by_id():
     response = requests.get(helper.base_url + "/2")
     first_activity = response.json()

     assert response.status_code == 200
     
     assert first_activity["ID"] == 2
     assert first_activity["Title"] == 'Activity 2'
     assert re.match(helper.pattern_date_time, first_activity["DueDate"])
     assert first_activity["Completed"] == True

def test_get_activity_wiyh_invalid_id_status_code_equals_400():
     response = requests.get(helper.base_url + "/a")

     assert response.status_code == 400