from flask import render_template, flash, redirect, url_for
from . import main
from .forms import RegistrationForm

# Integrate the Models in Routes
from . import db
from .models import User

@main.route('/', methods=['GET', 'POST'])
def index():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Hello, {form.username.data}!")
        return redirect(url_for("main.index"))
    return render_template("index.html", form=form)


@main.route('/add_user', methods=['POST'])
def add_user():
    user = User(username='JohnDoe', email='john@example.com')
    db.session.add(user)
    db.session.commit()
    return "User added!"