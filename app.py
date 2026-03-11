from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
  return "MERHABA, BULUTTAN SELAM"

@app.route('/about/')
def home():
  return "MERHABA, BULUTTAN SELAM"
