from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def index():
    number = random.randint(1, 6)
    return f"<h1>Ваше випадкове число: {number}</h1>"

if __name__ == "__main__":
    app.run()
