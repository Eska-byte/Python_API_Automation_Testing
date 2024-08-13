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
        "gender": "",
        "email": random_email,
        "status": "inactive"
    }
    req = requests.post(api_user, headers=head, json=payload)
    print(req.json())

    #VALIDATION
    status_code = req.status_code
    resp_field = req.json()[0]["field"]
    resp_message = req.json()[0]["message"]

    #ASSERT
    assert_that(status_code).is_equal_to(422)
    assert_that(resp_field).is_equal_to("gender")
    assert_that(resp_message).is_equal_to("can't be blank, can be male of female")

