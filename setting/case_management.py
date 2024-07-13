import requests

from setting.endpoint import TOKEN_QASE, PROJECT_CASE_QASE_IO, TEST_RUN_QASE_IO, api_result_qase_io


def update_test_result(test_case_id, status):
 #    setup header untuk hit endpoint qase
 headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Token": TOKEN_QASE
  }

 #  setup payload body untuk hit qase
 payload = {
    "case_id": test_case_id,
     "status": status
  }

 #  hit qase io
 req = requests.post(f"{api_result_qase_io}/{PROJECT_CASE_QASE_IO}/{TEST_RUN_QASE_IO}", headers=headers, json=payload)