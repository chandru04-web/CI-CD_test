# app.py
from flask import Flask,jsonify
import os

app = Flask(__name__)

@app.get("/")
def main():
    return jsonify({
        "message": "Hello from CI/CD test app!",
        "new push": "newly added",
        "env": {
            "APP_ENV": os.getenv("APP_ENV", "dev"),
            "GIT_SHA": os.getenv("GIT_SHA", "unknown")
        }
    })

if __name__ == "__main__":
    
    app.run(host='0.0.0.0', port=5000)
