from flask import render_template, url_for
from flaskdash import app
from flaskdash.forms import UpdateAccountForm
import flaskdash.chartjs as cjs

current_user = {'username': 'User', 'email': 'user@example.com'}


@app.route("/")
@app.route("/home")
@app.route("/dashboard")
def dashboard():
    config_bar = cjs.bar()
    config_doughnut = cjs.doughnut()
    return render_template('dashboard.html', title='Dashboard', config_bar=config_bar, config_doughnut=config_doughnut, current_user=current_user)


@app.route("/analytics")
def analytics():
    config_polar = cjs.polar()
    config_mixed = cjs.mixed()
    config_line = cjs.line()
    return render_template('analytics.html', title='Analytics', config_polar=config_polar, config_mixed=config_mixed, config_line=config_line, current_user=current_user)


@app.route("/account", methods=['GET', 'POST'])
def account():
    form = UpdateAccountForm()
    form.username.data = current_user['username']
    form.email.data = current_user['email']
    return render_template('account.html', title='Account', form=form, current_user=current_user)


@app.route("/help")
def help():
    return render_template('help.html', title='Help', current_user=current_user)
