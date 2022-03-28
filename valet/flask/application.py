import random;
from flask import Flask, render_template

app = Flask(__name__)


number=random.randint(1,10)
@app.route("/")

def index():
  return render_template('index.html',number=number)
  
@app.route('/goodbye')
def bye():
  return 'Good Bye'