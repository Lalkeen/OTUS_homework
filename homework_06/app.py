from os import getenv

from flask import Flask
from flask import request
from flask import render_template

from flask_migrate import Migrate
from flask_wtf import CSRFProtect

from models import db
from views.content import content_app

app = Flask(__name__)
app.register_blueprint(content_app)

config_class_name = getenv("CONFIG_CLASS", "Config")
config_object = f"config.{config_class_name}"
app.config.from_object(config_object)

db.init_app(app)
migrate = Migrate(app=app, db=db)
csrf = CSRFProtect(app)


@app.get("/")
def index_page():
    return render_template("index.html", textos="It's Home page")


@app.get("/about/")
def about_path():
    return render_template("about.html", textos="It's about page")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
