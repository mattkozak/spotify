from flask import render_template, jsonify, session, request, redirect, url_for
from app import app
#from .api import *

@app.route("/")
def home():
    return "Hello World!"

