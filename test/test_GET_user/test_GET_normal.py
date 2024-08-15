import pytest
import requests
from assertpy import assert_that
from setting.endpoint import api_user

@pytest.mark.QaseIO(10)
def test():
    head = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer 0c442a3b6e18178b523f54c1a375ad26b6d01afa7eaa1e12a55f7b972dbfd39b"
    }
    req = requests.get(api_user, headers=head)

    #VALIDATION
    status_code = req.status_code
    resp_id = req.json()[1]["id"]
    resp_name = req.json()[1]["name"]
    resp_email = req.json()[1]["email"]
    resp_gender = req.json()[1]["gender"]
    resp_status = req.json()[1]["status"]

    #ASSERT
    assert_that(status_code).is_equal_to(2001)
    assert_that(resp_id).is_not_none()
    assert_that(resp_id).is_type_of(int)
    assert_that(resp_name).is_not_none()
    assert_that(resp_email).is_not_none()
    assert_that(resp_email).contains("@")
    assert_that(resp_gender).is_not_none()
    assert_that(resp_gender).is_in("male","female")
    assert_that(resp_status).is_not_none()
    assert_that(resp_status).is_in("active","inactive")
