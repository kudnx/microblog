from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Kud'}
    posts = [
        {
            'author': {'username': 'kyouhime'},
            'body': 'I Love my husband kud!'
        },
        {
            'author': {'username': 'grea'},
            'body': 'the sky is so vast!'
        }
    ]
    return render_template('index.html', title='Página Inicial', user=user, posts=posts)

