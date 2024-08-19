# Update the Route to Handle the Form
from flask import render_template, flash, redirect, url_for
from . import main
from .forms import RegistrationForm


@main.route('/', methods=['GET', 'POST'])
def index():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Hello, {form.username.data}!")
        return redirect(url_for("main.index"))
    return render_template("index.html", form=form)