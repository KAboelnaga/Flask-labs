from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

class NameForm(FlaskForm):
    name = StringField('Enter your name:', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/')
def hello():
    return "Hello, Flask!"

@app.route('/user/<username>')
def user(username):
    return render_template('user.html', username=username)

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = NameForm()
    name = None
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('form.html', form=form, name=name)

if __name__ == '__main__':
    app.run(debug=True)
