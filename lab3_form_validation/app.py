from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecret'

class UserForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    age = IntegerField("Age", validators=[DataRequired(), NumberRange(min=1, max=120)])
    submit = SubmitField("Submit")

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UserForm()
    name = None
    age = None
    if form.validate_on_submit():
        name = form.name.data
        age = form.age.data
        form.name.data = ''
        form.age.data = ''
    return render_template("form.html", form=form, name=name, age=age)

if __name__ == "__main__":
    app.run(debug=True)
