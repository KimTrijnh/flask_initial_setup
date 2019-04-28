#routes for main_blueprint package
from datetime import datetime
from flask import render_template, redirect, url_for, session
from . import main
from .forms import NameForm
from .. import db
from ..models import *

@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():

        return redirect(url_for('.index'))
    return render_template('index.html', form = form, name=session.get('name'), known=session.get('known', False), current_time=datetime.utcnow())