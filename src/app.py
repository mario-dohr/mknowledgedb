from flask import Flask, render_template
from flask_mongoengine import MongoEngine
import model

app = Flask(__name__, template_folder='../templates', instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev'
)

app.config["MONGODB_SETTINGS"] = {
    "db": "mknowledgedb",
    "host": "localhost",
    "port": 27017
}
db = MongoEngine(app)


@app.route('/')
def main():
    p = model.Page.objects
    return render_template('main.html', pages=p)
