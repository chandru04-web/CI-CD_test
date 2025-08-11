# app.py
from flask import Flask,jsonify
import os

app = Flask(__name__)

@app.get("/")
def main():
    return jsonify({
        "message": "Hello from CI/CD test app!",
        "env": {
            "APP_ENV": os.getenv("APP_ENV", "dev"),
            "GIT_SHA": os.getenv("GIT_SHA", "unknown")
        }
    })

if __name__ == "__main__":
    # Only for local debugging, in container we'll use gunicorn
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=True)
