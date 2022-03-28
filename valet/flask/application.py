import random
# from urllib import request;
from flask import Flask, render_template,request

app = Flask(__name__)


number=random.randint(1,10)
@app.route("/")

def index():
  return render_template('index.html',number=number)

@app.route('/goodbye')
def bye():
  return 'Good Bye'

@app.route('/hello')
def hello():
  name = request.args.get('name')
  if not name:
    return render_template('faliure.html')
  return render_template('hello.html', name=name)