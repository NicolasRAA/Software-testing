# Verifiying integration 'Flask <-> DB <-> template'

import pytest
from app import app, db, Todo

# Flask test client with a fresh DB for each test
@pytest.fixture
def client():
    
    # Enabeling testing mode
    app.config["TESTING"] = True

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


def test_homepage_returns_200(client):
    """Homepage should respond with HTTP 200 OK"""
    response = client.get("/")
    assert response.status_code == 200


def test_homepage_shows_header_and_form(client):
    """
    Homepage should render the main header and the to-do form

    ASserting on static texts that come from app/templates/base.html:
      - <h1 class="ui center aligned header">To Do App</h1>
      - <label>Todo Title</label>
      - The "Add" submit button
    """
    response = client.get("/")
    html = response.data

    # H1 header text
    assert b"To Do App" in html

    # Label of the form field
    assert b"Todo Title" in html

    # Text of the submit button
    assert b"Add" in html
