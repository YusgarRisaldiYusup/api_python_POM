# tambahkan apabila gagal menemukan package proyek
import sys
import os

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from  assertpy import assert_that
import requests

from setting.endpoint import api_user

# memberikan mark id berdasarakan id di qaseio
@pytest.mark.QaseIO(5)
def test_1():
    # inisialisasi header
    head = {
        'Accept' : 'application/json',
        'Content-Type' : 'application/json',
        'Authorization' : 'bearer 0a169a5976f1eaf948eebc375c879a1422812aae6ffda94e9ce18214b54d1daf'
    }
    # hit api dan pemanggilan end point
    req = requests.get(api_user, headers=head)

    print(req.json())

    #Validator
    status_code = req.status_code
    resp_id = req.json()[0]['id']
    resp_name = req.json()[0]['name']
    resp_email = req.json()[0]['email']
    resp_status = req.json()[0]['status']

    #Assert
    assert_that(status_code).is_equal_to(200)
    assert_that(resp_id).is_not_none()
    assert_that(resp_id).is_type_of(int)
    assert_that(resp_name).is_not_none()
    assert_that(resp_email).is_not_none()
    assert_that(resp_email).contains('@')
    assert_that(resp_status).is_not_none()
    assert_that(resp_status).is_type_of(str)
    assert_that(resp_status).is_in("active", "inactive")