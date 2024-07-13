# tambahkan apabila gagal menemukan package proyek
import sys
import os

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from  assertpy import assert_that
import requests
# library faker untuk membuat email palsu
from faker import Faker
fake = Faker()

from setting.endpoint import api_user

# memberikan mark id berdasarakan id di qaseio
@pytest.mark.QaseIO(1)
def test_1():
    # inisialisasi random machine
    random_name = ""
    random_email = fake.email()
    # insialisasi payload
    payload = {
        "name": random_name,
        "gender": "male",
        "email": random_email,
        "status": "active"
    }
    # inisialisasi header
    head = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer 0a169a5976f1eaf948eebc375c879a1422812aae6ffda94e9ce18214b54d1daf'
    }
    # hit api dan pemanggilan end point
    req = requests.post(api_user, headers=head, json=payload)

    print(req.json())

    #Validator
    status_code = req.status_code
    resp_fld = req.json()[0]['field']
    resp_msg = req.json()[0]['message']


    #Assert
    assert_that(status_code).is_equal_to(422)
    assert_that(resp_fld).is_equal_to('name')
    assert_that(resp_msg).is_equal_to("can't be blank")
