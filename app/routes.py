from flask import render_template
from app import myapp


@myapp.route('/')
@myapp.route('/index')
def index():
    user_input = {'username': 'Miguel'}
    posts_input = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    secretkey_input = myapp.config['SECRET_KEY']

    return render_template('index.html', title='Home', user=user_input, posts=posts_input, secretkey=secretkey_input)



