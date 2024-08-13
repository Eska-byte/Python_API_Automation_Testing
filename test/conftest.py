import pytest


@pytest.fixture(scope='function', autouse=True)
def hooks_function(request):
    #before test
    print("\nBefore Test")

    yield
    #after test
    print("\nAfter Test")

@pytest.fixture(scope='session', autouse=True)
def hooks_suite(request):
    #before suite
    print("\nBefore Suite")

    yield
    #after suite
    print("\nAfter Suite")