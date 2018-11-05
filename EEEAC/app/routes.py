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
@app.route('/about')
def about():
    title = {'title': 'About'}
    return render_template('about.html')

@app.route('/ExecutiveBoard')
def executiveBoard(name):
    title = {'title': 'Executive Board'}
    return redirect(url_for('executiveBoard.html'))

@app.route('/ReviewCommittees')
def reviewCommittees(name):
    title = {'title': 'Review Committees'}
    return redirect(url_for('reviewCommittees.html'))

@app.route('/Disclosure')
def disclosure(name):
    title = {'title': 'Disclosure'}
    return redirect(url_for('disclosure.html'))

@app.route('/Structure')
def structure(name):
    title = {'title': 'Structure'}
    return redirect(url_for('structure.html'))

# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*
# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%           CONTACT US          %*%*%*%*%*%*%*%*%*%*%*%*%*%*
# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*

@app.route('/Contact')
def contact():
    title = {'title': 'Contact Us'}
    return redirect(url_for('Contact.html'))

# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*
# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%           REPORTS          %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%
# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*

@app.route('/Reports')
def reports():
    title = {'title': 'Reports'}
    return redirect(url_for('reports.html'))

# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*
# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%           LOGIN          %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%
# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*


