# Flask Application

from flask import Flask, render_template

app = Flask()

@app.route('/')
def index():
    return 'Hello'