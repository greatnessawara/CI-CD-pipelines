from flask import Flask, jsonify
import os

app = Flask(__name__)

ENV = os.getenv("APP_ENV", "development")

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to my DevOps Pipeline Demo!",
        "environment": ENV,
        "status": "running"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "environment": ENV
    }), 200

@app.route("/version")
def version():
    return jsonify({
        "version": "1.0.0",
        "environment": ENV
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
