from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import csv



app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

coffee_choices = [
    ("☕", "☕"),
    ("☕☕", "☕☕"),
    ("☕☕☕", "☕☕☕"),
    ("☕☕☕☕", "☕☕☕☕")
]
wifi_choices = [
    ("💪", "💪"),
    ("💪💪", "💪💪"),
    ("💪💪💪","💪💪💪"),
    ("💪💪💪💪","💪💪💪💪")
]
power_choices = [
    ("🔌", "🔌"),
    ("🔌🔌", "🔌🔌"),
    ("🔌🔌🔌","🔌🔌🔌"),
    ("🔌🔌🔌🔌","🔌🔌🔌🔌")
]

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField("Location", validators=[DataRequired()])
    open_time = StringField("Opening Time e.g. 8AM", validators=[DataRequired()])
    close_time = StringField("Closing Time e.g. 5:30PM", validators=[DataRequired()])
    coffee = SelectField("Coffee Rating", choices=coffee_choices)
    wifi = SelectField("WiFi Rating", choices=wifi_choices)
    power = SelectField("Power Outlet Rating", choices=power_choices)
    submit = SubmitField('Submit')



# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafe = form.cafe.data
        location = form.location.data
        open_time = form.open_time.data
        close_time = form.close_time.data
        coffee_rating = form.coffee.data
        wifi_rating = form.wifi.data
        power_rating = form.power.data
        with open("cafe-data.csv", "a", encoding="utf-8") as file:
            file.writelines(f"\n{cafe},{location},{open_time},{close_time},{coffee_rating},{wifi_rating},{power_rating}")
            return redirect("cafes")
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
