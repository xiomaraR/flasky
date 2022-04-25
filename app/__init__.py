from flask import Flask

def create_app():
    # __name__ stores the name of the module we're in
    app = Flask(__name__)

    from .routes import cat_routes, dog_routes

    app.register_blueprint(cat_routes.bp)
    app.register_blueprint(dog_routes.bp)

    return app