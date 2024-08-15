import json
from endpoint import WEBHOOK
import requests
from datetime import datetime


def slack_notif():
    json_content = open("report_all.json", "r").read()
    data_json = json.loads(json_content)
    datetime_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    try:
        test_passed = data_json.get("summary")["passed"]
    except:
        test_passed = "0"

    try:
        test_failed = data_json.get("summary")["failed"]
    except:
        test_failed = "0"

    try:
        test_total = data_json.get("summary")["total"]
    except:
        test_total = "0"

    test_success_rate = float(test_passed) / float(test_total) * 100

    if float(test_failed) > 1:
        color = "FF1E00"
    else:
        color = "3CFF29"

    payload = {
        "attachments": [
            {
                "color": f"{color}",
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
                        "type": "divider"
                    },
                    {
                        "type": "section",
                        "fields": [
                            {
                                "type": "mrkdwn",
                                "text": f"*Success Test:*\n {test_passed}"
                            },
                            {
                                "type": "mrkdwn",
                                "text": f"*Failed Test:*\n {test_failed}"
                            }
                        ]
                    },
                    {
                        "type": "section",
                        "fields": [
                            {
                                "type": "mrkdwn",
                                "text": "*Skipped Test:*\n0"
                            },
                            {
                                "type": "mrkdwn",
                                "text": f"*Total Test:*\n {test_total}"
                            }
                        ]
                    },
                    {
                        "type": "section",
                        "fields": [
                            {
                                "type": "mrkdwn",
                                "text": F"*Success Rate:*\n {test_success_rate}%"
                            }
                        ]
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "<https://google.com|Link Report Test>"
                        }
                    },
                    {
                        "type": "divider"
                    },
                    {
                        "type": "rich_text",
                        "elements": [
                            {
                                "type": "rich_text_section",
                                "elements": [
                                    {
                                        "type": "text",
                                        "text": "tested by : SUKMA KURNIA MUSTIKA",
                                        "style": {
                                            "italic": True
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "rich_text",
                        "elements": [
                            {
                                "type": "rich_text_section",
                                "elements": [
                                    {
                                        "type": "text",
                                        "text": f"created at : {datetime_now}",
                                        "style": {
                                            "italic": True
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ]

    }

    req = requests.post(WEBHOOK, json=payload)

slack_notif()
