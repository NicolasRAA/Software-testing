import pytest
from app import app, db

# Flask test client with a fresh DB for each test
@pytest.fixture
def client():
    
    # Enabeling testing mode
    app.config["TESTING"] = True
    # Provides a Flask test client to make HTTP requests

    # Dorping anc creating clean DB before each test
    with app.app_context():
        db.drop_all()
        db.create_all()

    # Providing the Flask test client to the test
    with app.test_client() as client:
        yield client

    # Cleanup after testing
    with app.app_context():
        db.drop_all()