from flask import Flask
import logging
import time

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    app.logger.info("Home page accessed.")
    return "Hello from Flask app with logging!"

if __name__ == "__main__":
    while True:
        app.logger.info("App is running...")
        time.sleep(10)
