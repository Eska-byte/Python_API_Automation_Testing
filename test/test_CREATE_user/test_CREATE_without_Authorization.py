import pytest
import requests
from assertpy import assert_that
from setting.endpoint import api_user
from faker import Faker
fake = Faker()

@pytest.mark.QaseIO(8)
def test():
    random_name = fake.name()
    random_email = fake.email()

    payload = {
        "name": random_name,
        "gender": "female",
        "email": random_email,
        "status": "inactive"
    }
    req = requests.post(api_user, json=payload)

    #VALIDATION
    status_code = req.status_code
    resp_message = req.json().get("message")

    #ASSERT
    assert_that(status_code).is_equal_to(401)
    assert_that(resp_message).is_equal_to("Authentication failed")
