from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def tasks():
  return 'tasks'

@app.route("/add")
def add():
  return 'add a new task'