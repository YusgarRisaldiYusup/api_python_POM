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

# =============== membuat user baru  ===============
# memberikan mark id berdasarakan id di qaseio
@pytest.mark.QaseIO(6)
def test_1():
    # inisialisasi random machine
    random_name = fake.name()
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

    print(f"ini adalah hasil create : {req.json()}")

    # =============== mengambil id user baru  ===============
    id_new_user = req.json().get('id')

    # =============== update data user baru  ===============
    random_name_update = fake.name()
    random_email_update = fake.email()

# insialisasi payload
    payload = {
    "name": random_name_update,
    "gender": "male",
    "email": random_email_update,
    "status": "active"
}

    # inisialisasi header
    head = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer 0a169a5976f1eaf948eebc375c879a1422812aae6ffda94e9ce18214b54d1daf'
    }

    # hit api
    req = requests.patch(f"{api_user}/{id_new_user}", headers=head, json=payload)
    print(f"ini adalah hasil update {req.json()}")


    #Validator
    status_code = req.status_code
    resp_id = req.json().get('id')
    resp_name = req.json().get('name')
    resp_email = req.json().get('email')
    resp_status = req.json().get('status')

    #Assert
    assert_that(status_code).is_equal_to(200)
    assert_that(resp_name).is_equal_to(random_name_update)
    assert_that(resp_email).is_equal_to(random_email_update)
    assert_that(resp_email).contains('@')
    assert_that(resp_status).is_not_none()
    assert_that(resp_status).is_type_of(str)
    assert_that(resp_status).is_in("active", "inactive")