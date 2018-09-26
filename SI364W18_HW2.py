## SI 364
## Winter 2018
## HW 2 - Part 1
## Olivia Gardella

## This homework has 3 parts, all of which should be completed inside this file (and a little bit
## inside the /templates directory).

## Add view functions and any other necessary code to this Flask application code below so that
## the routes described in the README exist and render the templates they are supposed to (all
## templates provided are inside the templates/ directory, where they should stay).

## As part of the homework, you may also need to add templates (new .html files) to the templates directory.

#############################
##### IMPORT STATEMENTS #####
#############################
from flask import Flask, request, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, ValidationError
from wtforms.validators import Required

#####################
##### APP SETUP #####
#####################

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hardtoguessstring'

####################
###### FORMS #######
####################




####################
###### ROUTES ######
####################

# in original file - do not change
@app.route('/')
def hello_world():
    return 'Hello World!'

# in original file - do not change
@app.route('/user/<name>')
def hello_user(name):
    return '<h1>Hello {0}<h1>'.format(name)

#
@app.route('/artist_info')
def artist_info:
    pass

#
@app.route('/artist_links')
def artist_links:
    pass

#
@app.route('/artistform')
def artistform:
    pass

#
@app.route('/specific_artist')
def specific_artist:
    pass




if __name__ == '__main__':
    app.run(use_reloader=True,debug=True)
