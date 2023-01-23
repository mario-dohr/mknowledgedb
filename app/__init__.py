from flask import Flask
from model import db

# new comment
def create_app():
    app = Flask(__name__, template_folder='../templates', instance_relative_config=True)
    app.logger.info('create_app')
    app.config.from_mapping(
        SECRET_KEY='dev'
    )
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

    db.init_app(app)

    from main import main_bp
    import main
    app.register_blueprint(main_bp)

    return app


