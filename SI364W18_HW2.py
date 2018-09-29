## SI 364
## Winter 2018
## HW 2 - Part 1
## Olivia Gardella

## Worked with: Emma Welch

## This homework has 3 parts, all of which should be completed inside this file (and a little bit
## inside the /templates directory).

## Add view functions and any other necessary code to this Flask application code below so that
## the routes described in the README exist and render the templates they are supposed to (all
## templates provided are inside the templates/ directory, where they should stay).

## As part of the homework, you may also need to add templates (new .html files) to the templates directory.

#############################
##### IMPORT STATEMENTS #####
#############################
from flask import Flask, request, render_template, url_for, flash, redirect
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

class AlbumEntryForm(FlaskForm):
    album_name = StringField('Enter the name of an album:', validators=[Required()])
    rating = RadioField('How much do you like this album? (1 low, 3 high)', choices = [('1','1'),('2','2'),('3','3')], validators=[Required()])
    submit = SubmitField('Submit')

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


#### Part 1 ####

### DONE
# route for form in artistform.html
@app.route('/artistform')
def artistform():
    return render_template('artistform.html')

### DONE
# route for once form is sumbitted, uses artist_info.html, need to use itunes api
@app.route('/artistinfo', methods = ['GET'])
def artist_info():
    if request.method == 'GET':
        base_url = 'https://itunes.apple.com/search?'
        params_diction = {}
        params_diction['term'] = request.args.get('artist')
        response = requests.get(base_url, params = params_diction)
        response_text = json.loads(response.text)
        response_py = response_text['results']
        return render_template('artist_info.html', objects = response_py)
    flash('Must enter an artist')
    return redirect(url_for('albumform'))

### DONE
# route to artist_links
@app.route('/artistlinks')
def artist_links():
    return render_template('artist_links.html')

### DONE
# route for spcific_artist.html
@app.route('/specific/song/<artist_name>')
def specific_song(artist_name):
    base_url = 'https://itunes.apple.com/search'
    params_diction = {}
    params_diction['term'] = artist_name
    response = requests.get(base_url, params = params_diction)
    text = response.text
    python_obj = json.loads(text)
    result_py = python_obj['results']
    return render_template('specific_artist.html', results = result_py)


#### Parts 2+3 ####

### DONE
# route for album_entry.html
@app.route('/album_entry')
def album_entry():
    # return ('hi')
    form = AlbumEntryForm()
    return render_template('album_entry.html', form=form)

### DONE
# route for album_data.html
@app.route('/album_result', methods=['GET','POST'])
def album_result():
    form = AlbumEntryForm()
    if request.method == 'POST' and form.validate_on_submit():
        album = form.album_name.data
        rating = form.rating.data
        return render_template('album_data.html', album=album, rating=rating)
    flash('Must enter all fields')
    return redirect(url_for('album_entry'))


# must keep at end
if __name__ == '__main__':
    app.run(use_reloader=True,debug=True)
