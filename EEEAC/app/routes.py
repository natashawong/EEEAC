from app import app
from flask import render_template, redirect, url_for
from .forms import SearchForm, AddForm

# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%
# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%           HOME          %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%
# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%

@app.route('/')
def home():
    return render_template('index.html')

# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*
# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%           ABOUT US          %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*
# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*

tempAddData = []
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/ExecutiveBoard')
def executiveBoard(name):
    return redirect(url_for('executiveBoard.html'))

@app.route('/ReviewCommittees')
def reviewCommittees(name):
    return redirect(url_for('reviewCommittees.html'))

@app.route('/Disclosure')
def disclosure(name):
    return redirect(url_for('disclosure.html'))

@app.route('/Structure')
def structure(name):
    return redirect(url_for('structure.html'))

# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*
# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%           CONTACT US          %*%*%*%*%*%*%*%*%*%*%*%*%*%*
# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*

@app.route('/Contact')
def contact():
    return redirect(url_for('Contact.html'))

# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*
# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%           REPORTS          %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%
# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*

@app.route('/Reports')
def reports():
    return redirect(url_for('reports.html'))

# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*
# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%           LOGIN          %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%
# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*


