import pytest

@pytest.fixture(scope="session", name="page")
def get_page():
    with open("tests/data/page.json", "r") as f:
        yield f.read()


@pytest.fixture(scope="session", name="database")
def get_database():
    with open("tests/data/database.json", "r") as f:
        yield f.read()
