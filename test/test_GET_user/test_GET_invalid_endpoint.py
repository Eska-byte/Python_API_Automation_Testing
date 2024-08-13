import requests
from assertpy import assert_that
from setting.endpoint import api_user_wrong


def test():
    head = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer 0c442a3b6e18178b523f54c1a375ad26b6d01afa7eaa1e12a55f7b972dbfd39b"
    }
    req = requests.get(api_user_wrong, headers=head)

    #VALIDATION
    status_code = req.status_code

    #ASSERT
    assert_that(status_code).is_equal_to(404)
