# tambahkan apabila gagal menemukan package proyek
import sys
import os

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from  assertpy import assert_that
import requests

from setting.endpoint import  api_user_wrong

# memberikan mark id berdasarakan id di qaseio
@pytest.mark.QaseIO(4)
def test_1():
    # inisialisasi header
    head = {
        'Accept' : 'application/json',
        'Content-Type' : 'application/json',
        'Authorization' : 'bearer 0a169a5976f1eaf948eebc375c879a1422812aae6ffda94e9ce18214b54d1daf'
    }
    # hit api dan pemanggilan end point
    req = requests.get(api_user_wrong, headers=head)

    #Validator
    status_code = req.status_code


    #Assert
    assert_that(status_code).is_equal_to(404)
