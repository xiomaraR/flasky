from unicodedata import name
import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.dogs import Dog


@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def two_dogs(app):
    roscoe = Dog(id=1, name="Roscoe", age=7)
    snowpuff = Dog(id=2, name="Snowpuff", age=3)

    db.session.add(roscoe)
    db.session.add(snowpuff)
    db.session.commit()