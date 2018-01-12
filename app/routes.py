<<<<<<< HEAD
# -*- coding: utf-8 -*-
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Эльдар Рязанов'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Иполит'},
            'body': 'Какая гадость эта ваша заливная рыба!!'
        }
        {
            'author': {'username': 'Царь'},
            'body': 'Какое житие твое пёс смердячий!!'
        }
        {
            'author': {'username': 'Шпак'},
            'body': 'Три магнитофона!!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
=======
# -*- coding: utf-8 -*-
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Эльдар Рязанов'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Иполит'},
            'body': 'Какая гадость эта ваша заливная рыба!!'
        }
        {
            'author': {'username': 'Царь'},
            'body': 'Какое житие твое пёс смердячий!!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
>>>>>>> 27f16f7b902858791a5010044be3d1f0217799a5
