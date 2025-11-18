#Testing for todo CRUD operations: add, complete, delete todos

from app import app, db, Todo


def test_add_todo_creates_item_and_displays_it(client):
    """
    Integration test for creating a new todo via POST /add

    The test goes through:
        - Flask routing and form handling (POST /add)
        - DB write via SQLAlchemy (creating a Todo row)
        - Redirect back to "/" and rendering of the updated HTML page
    """
    # Act: sending a POST request to /add with a form field "title"
    response = client.post(
        "/add",
        data={"title": "Finish the otchet"},
        follow_redirects=True,  # following redirect back to "/"
    )

    # Assert: final response after redirect should be 200 OK
    assert response.status_code == 200

    # Assert on the DB state
    with app.app_context():
        todos = Todo.query.all()
        assert len(todos) == 1
        assert todos[0].title == "Finish the otchet"
        assert todos[0].complete is False

    # Assert on the HTML: the new todo title should be visible
    html = response.data
    assert b"Finish the otchet" in html
    assert b"Not Complete" in html  # label from base.html for incomplete todos


def test_complete_todo_marks_item_as_completed(client):
    """
    Integration test for marking a todo as completed via /update/<id>

    The test goes through:
        - Existing data in the DB (pre-populated Todo)
        - Flask routing for /update/<id>
        - Db update via SQLAlchemy (toggling 'complete')
        - Redirect back to "/" and rendering of the updated HTML
    """
    # Arrange: creating a todo directly in the database
    with app.app_context():
        todo = Todo(title="Study integration testing", complete=False)
        db.session.add(todo)
        db.session.commit()
        todo_id = todo.id

    # Act: calling /update/<id> and following the redirect to "/"
    response = client.get(f"/update/{todo_id}", follow_redirects=True)
    assert response.status_code == 200

    # Assert on the database state: the todo should now be completed
    with app.app_context():
        updated_todo = db.session.get(Todo, todo_id)
        assert updated_todo is not None
        assert updated_todo.complete is True

    # Assert on the HTML: the "Completed" label should be visible
    html = response.data
    assert b"Completed" in html
    # Asserting that "Not Complete" is no longer present
    assert b"Not Complete" not in html


def test_delete_todo_removes_item_from_database_and_page(client):
    """
    Integration test for deleting a todo via /delete/<id>

    This test goes through:
        - Existing data in the DB (pre-populated Todo)
        - Flask routing for /delete/<id>
        - DB delete via SQLAlchemy
        - Redirect back to "/" and rendering of the updated HTML
    """
    # Arrange: creating a todo directly in the DB
    with app.app_context():
        todo = Todo(title="Do lab3 for software-testing", complete=False)
        db.session.add(todo)
        db.session.commit()
        todo_id = todo.id

    # Act: calling /delete/<id> and following the redirect to "/"
    response = client.get(f"/delete/{todo_id}", follow_redirects=True)
    assert response.status_code == 200

    # Assert on the DB: the todo should be removed
    with app.app_context():
        deleted_todo = db.session.get(Todo, todo_id)
        assert deleted_todo is None
        assert Todo.query.count() == 0

    # Assert on the HTML: the title should no longer be present
    html = response.data
    assert b"Clean room" not in html
