# Trying edge cases: adding a todo with empty title, and updating an unexisting todo

from app import app, db, Todo


def test_add_todo_allows_empty_title(client):
    """
    Creating a todo with an empty title

    The current implementation of /add does not validate the title,
    so an empty string is still stored in the DB;
    This test documents the current behavior and can be used later
    as a basis for improving validation and input handling
    """
    # Act: sending POST request with an empty title
    response = client.post(
        "/add",
        data={"title": ""},
        follow_redirects=True,
    )

    # The request still succeeds and redirects back to "/"
    assert response.status_code == 200

    # Assert on DB state: one todo with an empty title
    with app.app_context():
        todos = Todo.query.all()
        assert len(todos) == 1
        assert todos[0].title == ""
        assert todos[0].complete is False

    # Assert on HTML: the empty title is rendered, tho it maay appear as blank
    html = response.data
    # Checking that the "Not Complete" laibel is present for the created todo
    assert b"Not Complete" in html


def test_update_nonexistent_todo_triggers_server_error(client):
    """
    Calling /update/<id> for a non-existing todo

    The current implementation does not handle the "not found" case:
        - Todo.query.filter_by(id=todo_id).first() returns None
        - the code tries to access attributes on None, which leads to an error

    As a result, updating a missing id leads to a server error -> HTTP 5xx
    This test exposes a robustness isue in the integration between the
    web layer and the data layer
    """
    # Act: calling /update on an ID that does not exist in the DB
    response = client.get("/update/9999")

    # Expecting a 5xx error due to missing null-check in the code
    assert 500 <= response.status_code < 600
