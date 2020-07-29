@pytest.fixture
def test_email(request):
    try:
        params = request.param
        if params == "free":
            return Faker().ascii_free_email()
        elif params == "company":
            return Faker().ascii_company_email()
        else:
            logger.warning(f"incorrect request param:{params}")
            return Faker().email()
    except AttributeError:
        return Faker().email()