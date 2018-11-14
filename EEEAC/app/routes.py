from app import app
from flask import render_template, redirect, url_for
from .forms import SearchForm, AddForm

# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%
# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%           HOME          %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%
# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%

@app.route('/')
def home():
    title = {'title': 'Home'}
    return render_template('index.html')

# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*
# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%           ABOUT US          %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*
# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*

tempAddData = []
@app.route('/ExecutiveBoard')
def executiveBoard(name, title):
    title = {'title': 'Executive Board'}
    return render_template('executiveBoard.html'))

@app.route('/ReviewCommittees')
def reviewCommittees(name, title):
    title = {'title': 'Review Committees'}
    return render_template('reviewCommittees.html'))

@app.route('/Disclosure')
def disclosure(name, title):
    title = {'title': 'Disclosure'}
    return render_template('disclosure.html'))

@app.route('/Structure')
def structure(name, title):
    title = {'title': 'Structure'}
    return render_template('structure.html'))

# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*
# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%           CONTACT US          %*%*%*%*%*%*%*%*%*%*%*%*%*%*
# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*

@app.route('/Contact')
def contact(title):
    title = {'title': 'Contact Us'}
    return render_template('Contact.html'))

# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*
# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%           REPORTS          %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%
# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*

@app.route('/Reports')
def reports(title):
    title = {'title': 'Reports'}
    return render_template('reports.html'))

# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*
# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%           LOGIN          %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%
# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*
