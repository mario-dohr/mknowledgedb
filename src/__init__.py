import os

from flask import Flask, render_template
from flask_mongoengine import MongoEngine

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, template_folder='../templates', instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    #app.config["MONGO_URI"] = "mongodb://localhost:27017/mknowledgedb"
    app.config["MONGODB_SETTINGS"] = {
        "db": "mknowledgedb",
        "host": "localhost",
        "port": 27017
    }

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db = MongoEngine(app)

    # a simple page that says hello
    @app.route('/')
    def hello():
        from . import model

        #db.get_db().pages.insert_one({'title': 'juhu2'})
        #model.Page.objects(title='juhu')
        p = model.Page.objects

        return render_template('main.html', pages=p)

    return app
