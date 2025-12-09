from flask import Flask, render_template
from flask_migrate import Migrate
from models import db
from config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

@app.route("/login")
def login():
    return render_template("auth/login.html")

@app.route("/")
def index():
    return render_template("home/index.html")

if __name__ == "__main__":
    PORT=os.getenv("PORT")
    app.run(debug=True, port=PORT)