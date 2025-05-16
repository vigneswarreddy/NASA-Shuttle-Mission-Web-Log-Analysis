from flask import Flask, render_template, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from datetime import datetime
import socket
import os

app = Flask(__name__, template_folder='render_template')

# Set up rate limiting
limiter = Limiter(
    key_func=get_remote_address,
    app=app,
    default_limits=["500 per minute"]
)

# Helper function for logging requests
def log_request(path):
    container_id = socket.gethostname()
    os.makedirs("output", exist_ok=True)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open("output/server_log.txt", "a") as f:
        f.write(f"{timestamp} - Handled by: {container_id} (path: {path})\n")
    return container_id

@app.route('/')
def home():
    container_id = log_request("/")
    return render_template('index.html', container_id=container_id)

# Catch-all route for any path
@app.route('/<path:requested_path>')
def catch_all(requested_path):
    full_path = "/" + requested_path
    container_id = log_request(full_path)
    return render_template('index.html', container_id=container_id)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
