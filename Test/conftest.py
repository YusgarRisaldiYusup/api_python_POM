import pytest
from setting.case_management import update_test_result

@pytest.fixture(scope='function', autouse=True)
def hooks(request):
    # BEFORE TEST
    print('before test')
    get_error = request.session.testsfailed

    yield
    # AFTER TEST
    print('after test')
    status = request.session.testsfailed - get_error
    test_case_id = request.node.get_closest_marker("QaseIO").args[0]

    if status == 0:
        update_test_result(test_case_id, "passed")
    else:
        update_test_result(test_case_id, "failed")


@pytest.fixture(scope='session', autouse=True)
def suites(request):
    # BEFORE SUITE
    print('before suite')
    yield
    # AFTER SUITE
    print('after suite')
