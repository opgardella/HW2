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

import requests #added
import json #added

#####################
##### APP SETUP #####
#####################

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hardtoguessstring'

####################
###### FORMS #######
####################

# #create class to represent WTForm that inherits flask form
# class ArtistForm(FlaskForm):
#     artist = StringField('What is the artist name?', validators=[Required()])
#     num_results = IntegerField('How many results do you want to see?', validators=[Required()])
#     email = StringField('What is your email?', validators=[Required(),Email()])
#     submit = SubmitField('Submit')


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

# route for form in artistform.html
@app.route('/artistform')
def artistform():
    # simpleForm = ArtistForm()
    return render_template('artistform.html')
    # return render_template('artistform.html', form=simpleForm)

# route for once form is sumbitted, uses artist_info.html, need to use itunes api
@app.route('/artistinfo', methods = ['GET', 'POST'])
def artist_info():
    base_url = 'https://itunes.apple.com/search'
    params_diction = {}
    params_diction['term'] = form.request
    # params_diction['entity'] = 'musicArtist'
    response = requests.get(base_url, params = params_diction)
    text = response.text
    python_obj = json.loads(text)
    return str(python_obj)

    # base_url = "https://itunes.apple.com/search"
    # params_diction = {}
    # params_diction['term'] = movie
    # params_diction['entity'] = 'movie'
    # resp = requests.get(base_url,params=params_diction)
    # text = resp.text
    # python_obj = json.loads(text)
    # return str(python_obj)

    # form = ArtistForm(request.form)
    # params_diction = {}
    # if request.method == 'POST' and form.validate_on_submit():
    #     params_diction['term'] = form.artist.data
    #     params_diction['limit'] = form.num_results.data #basically request.args.get('num_results')
    #     email = form.email.data
    #     response = requests.get('https://itunes.apple.com/search', params = params_diction)
    #     response_text = json.loads(response.text)
    #     result_py = response_text['results']
    #     return render_template('itunes-results.html', result__html = result_py)
    # flash('All fields are required!')
    # return redirect(url_for('itunes_form')) #this redirects you to itunes_form if there are errors


# route to artist_links
@app.route('/artistlinks')
def artist_links():
    return render_template('artist_links.html')




# #
# @app.route('/specific_artist')
# def specific_artist():
#     pass




if __name__ == '__main__':
    app.run(use_reloader=True,debug=True)
