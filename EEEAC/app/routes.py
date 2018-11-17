from app import app
from flask import render_template, redirect, url_for
from .forms import SearchForm, AddForm

# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%
# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%           HOME          %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%
# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%

@app.route('/')
def home(title="Home"):
    return render_template('index.html', title=title)

# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*
# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%           ABOUT US          %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*
# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*

tempAddData = []
@app.route('/ExecutiveBoard')
def executiveBoard(title="Executive Board"):
    return render_template('executiveBoard.html', title=title)

@app.route('/ReviewCommittees')
def reviewCommittees(title="Review Committees"):
    return render_template('reviewCommittees.html', title=title)

@app.route('/Disclosure')
def disclosure(title="Disclosure"):
    return render_template('disclosure.html', title=title)

@app.route('/Structure')
def structure(title="Structure"):
    return render_template('structure.html', title=title)

# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*
# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%           CONTACT US          %*%*%*%*%*%*%*%*%*%*%*%*%*%*
# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*

@app.route('/Contact')
def contact(title="Contact"):
    return render_template('Contact.html', title=title)

# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*
# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%           REPORTS          %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%
# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*

@app.route('/Reports')
def reports(title="Reports"):
    return render_template('reports.html', title=title)

# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*
# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%           LOGIN          %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%
# %*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*%*
