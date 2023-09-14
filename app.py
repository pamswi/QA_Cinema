from flask import Flask
from application import app, db
#import os, requests









if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, debug=True)
