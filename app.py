from flask import Flask, render_template
from flask_migrate import Migrate
from models import db
from config import Config
import os

Config.validate_env()

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

@app.route("/login")
def login():
    return render_template("auth/login.html")

@app.route("/")
def home():
    return render_template("/home/homepage.html")

@app.errorhandler(404)
def not_found(error):
    return render_template("errors/404.html"), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template("errors/500.html"), 500


if __name__ == "__main__":
    PORT = int(os.getenv("PORT", 5055))
    DEBUG = os.getenv("FLASK_DEBUG", "False").lower() in ("true", "1", "yes")
    app.run(debug=DEBUG, port=PORT)