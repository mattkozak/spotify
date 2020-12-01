from flask import Flask, session

app = Flask(__name__)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

from app import routes
