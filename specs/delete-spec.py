import requests
import re

from helpers import helper

def test_delete_activity_status_code_equals_200():
     response = requests.delete(helper.base_url + "/1")
     assert response.status_code == 200

def test_delete_invalid_activity_status_code_equals_200():
     response = requests.delete(helper.base_url + "/a")
     assert response.status_code == 400