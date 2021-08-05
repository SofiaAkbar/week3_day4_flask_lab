from flask import render_template
from app import app
from models.event import *
from models.event_planner import *

@app.route('/events')
def index():
    return render_template('index.html', title='Home', events=events)