import pytest

from setting.case_management import update_test_result


@pytest.fixture(scope='function', autouse=True)
def hook(request):
    #before test
    print("\nBefore Test")
    get_error = request.session.testsfailed

    yield
    #after test
    print("\nAfter Test")
    test_status = request.session.testsfailed - get_error
    test_case_id = request.node.get_closest_marker("QaseIO").args[0]

    if test_status == 0:
        update_test_result(test_case_id, "passed")
    else:
        update_test_result(test_case_id, "failed")

@pytest.fixture(scope='session', autouse=True)
def suite(request):
    #before suite
    print("\nBefore All")

    yield
    #after suite
    print("\nAfter All")