from app import app
from flask import render_template,flash, redirect, url_for,jsonify, request

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Kritish Pahi'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Kritish', user=user, posts=posts) 


@app.route('/compute', methods=['GET', 'POST'])
def compute():
    
    form_data = request.form
    all_start_date = form_data.getlist('start')
    all_end_date = form.data.getlist('end')
    # import ipdb; ipdb.set_trace()
    # form = LoginForm()
    # if form.validate_on_submit():
    #     print(form)
    #     return redirect(url_for('compute'))
    return render_template('thanks.html')