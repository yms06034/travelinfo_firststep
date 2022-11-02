from flask import Blueprint, render_template
import pickle

NAME = 'base'

base_bp = Blueprint(NAME, __name__)

@base_bp.route('/')
def index():
    return render_template('index.html')