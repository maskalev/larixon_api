import pytest
from django.core.management import call_command


@pytest.fixture(autouse=True)
def load_initial_data():
    call_command("loaddata", "tests/fixtures/data.json")


@pytest.fixture
def flush_db():
    call_command("flush", interactive=False)


@pytest.fixture(autouse=True)
def cleanup_db(flush_db):
    yield
