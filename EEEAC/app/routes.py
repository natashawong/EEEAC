from app import app
from flask import render_template, redirect, url_for
from .forms import SearchForm, AddForm

# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%           HOME          %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%

@app.route('/')
def home():
    return render_template('home.html')

# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%           END HOME           %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%



# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%           STATUS           %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%

from app.Backend.Status import refresh

i = 0
@app.route('/Status')
def homeStatus():
    global i
    if i == 0:
        env = 'production'
        data, count, jinw = refresh(env)  # jinw = jinja workaround, count means count of boxes that need to be populated
        i = 1
        return render_template('status.html', Data=data, env=env, count=count, jinw=jinw)
    if i == 1:
        env = 'sales'
        data, count, jinw = refresh(env)
        i = 2
        return render_template('status.html', Data=data, env=env, count=count, jinw=jinw)
    if i == 2:
        env = 'internal'
        data, count, jinw = refresh(env)
        i = 0
        return render_template('status.html', Data=data, env=env, count=count, jinw=jinw)

# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%           END STATUS           %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%



# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%           BLACKLIST           %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%

from app.Backend.Blacklist import dataSearch, addtoDB, deleter

tempdata = []
@app.route('/Blacklist', methods=["GET", "POST"])
def homeBL():
    global tempdata
    form = SearchForm()
    if form.validate_on_submit():
        data = dataSearch(form.search.data)
        tempdata = data
    else:
        data = tempdata
    return render_template('blacklist.html', form=form, data=data)

@app.route('/delete/<name>')
def delete(name):
    deleter(name)
    global tempdata
    tempdata.remove(name)
    return redirect(url_for('homeBL'))

tempAddData = []
@app.route('/add', methods=["GET","POST"])
def append():               # named append so that it doesnt conflict with a python function
    form = AddForm()
    global tempAddData
    if form.validate_on_submit():
        tempAddData.append(form.add.data)
    return render_template('add.html', form=form, data=tempAddData)

@app.route('/deleteadd/<name>')
def deleteAdd(name):
    global tempAddData
    tempAddData.remove(name)
    return redirect(url_for('append'))

@app.route('/commit')
def commit():
    global tempAddData      #make set
    for i in tempAddData:
        addtoDB(i)
    tempAddData = []
    return redirect(url_for('homeBL'))

# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%          END BLACKLIST           %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%