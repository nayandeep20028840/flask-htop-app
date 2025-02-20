from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get system username
    username = os.getenv("USER") or os.getenv("USERNAME") or "Unknown"

    # Get server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S")

    # Get top command output
    top_output = subprocess.getoutput("top -b -n 1")

    # Format the response
    response = f"""
    <h1>Name: Nayan Deep</h1>
    <h2>Username: {username}</h2>
    <h2>Server Time: {server_time} IST</h2>
    <pre>{top_output}</pre>
    """
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
