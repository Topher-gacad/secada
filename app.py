from flask import Flask, render_template
from config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def home():
    return render_template("/home/homepage.html")

if __name__ == "__main__":
    PORT=os.getenv("PORT")
    app.run(debug=True, port=PORT)