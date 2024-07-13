# jangan jalanakan sebagai test, nanti reportnya berubah
# run dengan python + nama file, jangan pytest
#  cara send report ke slcak jalankan ini python namafolder/namfile.py

import json
from endpoint import WEBHOOK
import requests
# import waktu
from datetime import datetime

def notif_Slcak():
    jsonContent = open("report_all.json", "r").read()
    data_json = json.loads(jsonContent)
    date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(data_json.get("summary"))

    # agar report test dapat di run berkali kali dan berubah setiap run
    try:
     test_passed = data_json.get("summary")["passed"]
    except:
       test_passed = "0"

    try:
      test_failed = data_json.get("summary")["failed"]
    except:
         test_failed = "0"

    try:
        total_test = data_json.get("summary")["total"]
    except:
        total_test = "0"

    # membuat test_rate
    test_success_rate = (float(test_passed) / float(total_test)) * 100
    print(test_success_rate)

    # agar warna report dapat berubah ubah
    if  float(test_failed) > 1 :
        color = "FF1E00"
    else:
        color = "3CFF29"

    # diambil dari block kit builder
    payload = {
        "attachments": [
            {
                "color": F"{color}",
                "blocks": [
                    {
                        "type": "header",
                        "text": {
                            "type": "plain_text",
                            "text": "API AUTOMATION",
                            "emoji": True
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "plain_text",
                            "text": "Ini adalah hasil reporting API untuk 12/07/2024",
                            "emoji": True
                        }
                    },
                    {
                        "type": "section",
                        "fields": [
                            {
                                "type": "plain_text",
                                "text": f"*test_total = {total_test} *",
                                "emoji": True
                            },
                            {
                                "type": "plain_text",
                                "text": f"*test_failed = {test_failed}*",
                                "emoji": True
                            },
                            {
                                "type": "plain_text",
                                "text": f"*test_passed = {test_passed} *",
                                "emoji": True
                            },
                            {
                                "type": "plain_text",
                                "text": f"*Test_percentase = {test_success_rate} *",
                                "emoji": True
                            }
                        ]
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "This is a *<https://www.example.com|link report>*"
                        }
                    },
                    {
                        "type": "divider"
                    },
                    {
                        "type": "context",
                        "elements": [
                            {
                                "type": "plain_text",
                                "text": "Author: YusgarYRY",
                                "emoji": True
                            }
                        ]
                    },
                    {
                        "type": "context",
                        "elements": [
                            {
                                "type": "plain_text",
                                "text": f"Created at: {date_time}",
                                "emoji": True
                            }
                        ]
                    }
                ]
            }
        ]
    }

    req = requests.post(WEBHOOK, json=payload)


notif_Slcak()