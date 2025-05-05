import os
import socket
from flask import Flask

app = Flask(__name__)

@app.route('/')
def info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    author = os.getenv('AUTHOR', 'Unknown')
    return f"""
    <h1>Echo Server</h1>
    <p>Hostname: {hostname}</p>
    <p>IP Address: {ip_address}</p>
    <p>Author: {author}</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)