import requests
from assertpy import assert_that
from setting.endpoint import api_user
from faker import Faker
fake = Faker()

def test():
    random_name = fake.name()
    random_email = fake.email()

    head = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer 0c442a3b6e18178b523f54c1a375ad26b6d01afa7eaa1e12a55f7b972dbfd39b"
    }
    payload = {
        "name": random_name,
        "gender": "female",
        "email": random_email,
        "status": "inactive"
    }
    req = requests.post(api_user, headers=head, json=payload)

    #VALIDATION
    status_code = req.status_code
    resp_id = req.json().get("id")
    resp_name = req.json().get("name")
    resp_email = req.json().get("email")

    #ASSERT
    assert_that(status_code).is_equal_to(201)
    assert_that(resp_id).is_not_none()
    assert_that(resp_id).is_type_of(int)
    assert_that(resp_name).is_not_none()
    assert_that(resp_name).is_equal_to(random_name)
    assert_that(resp_email).is_not_none()
    assert_that(resp_email).is_equal_to(random_email)