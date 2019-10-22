from datetime import timedelta
from flask import Markup
from flask import Flask, request, render_template, url_for, session, redirect, g, jsonify
import os
import pymysql
from flask_googlecharts import GoogleCharts, MaterialLineChart, PieChart
from flask_googlecharts import BarChart
from flask_googlecharts.utils import prep_data
import datetime



app = Flask(__name__)
charts = GoogleCharts()
charts.init_app(app)

mysql_server="localhost"
# app.config.from_pyfile("config.cfg")
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/google-charts/pie-chart')
def google_pie_chart():
	data = {'Task' : 'Hours per Day', 'Work' : 11, 'Eat' : 2, 'Commute' : 2, 'Watching TV' : 2, 'Sleeping' : 7}
	#print(data)
	return render_template('pie-chart.html', data=data)

@app.route("/data")
def data():
    d = {"cols": [{"id": "", "label": "Date", "pattern": "", "type": "date"},
                  {"id": "", "label": "Spectators", "pattern": "", "type": "number"}],
         "rows": [{"c": [{"v": datetime.date(2016, 5, 1), "f": None}, {"v": 3987, "f": None}]},
                  {"c": [{"v": datetime.date(2016, 5, 2), "f": None}, {"v": 6137, "f": None}]},
                  {"c": [{"v": datetime.date(2016, 5, 3), "f": None}, {"v": 9216, "f": None}]},
                  {"c": [{"v": datetime.date(2016, 5, 4), "f": None}, {"v": 22401, "f": None}]},
                  {"c": [{"v": datetime.date(2016, 5, 5), "f": None}, {"v": 24587, "f": None}]}]}

    return jsonify(prep_data(d))

@app.route('/googlechart')
def chart2():
    hot_dog_chart = BarChart("hot_dogs", options={"title": "Contest Results",
                                                  "width": 500,
                                                  "height": 300})
    hot_dog_chart.add_column("string", "Competitor")
    hot_dog_chart.add_column("number", "Hot Dogs")
    hot_dog_chart.add_rows([["Matthew Stonie", 62],
                            ["Joey Chestnut", 60],
                            ["Eater X", 35.5],
                            ["Erik Denmark", 33],
                            ["Adrian Morgan", 31]])
    charts.register(hot_dog_chart)
    spectators_chart = MaterialLineChart("spectators",
                                         options={"title": "Contest Spectators",
                                                  "width": 500,
                                                  "height": 300},
                                         data_url=url_for('data'))

    charts.register(spectators_chart)
    pie_chart= PieChart("pie_chart",options={"title":"Daily routine",
                                        "width":500,
                                        "height":300})
    pie_chart.add_column("string","Task")
    pie_chart.add_column("number","Hours per day")
    pie_chart.add_rows([["Eat",2],
                        ["Study",3],
                        ["College",10],
                        ["Sleep",7],
                       ["others",3]])
    charts.register(pie_chart)
    return render_template("GoogleChart.html")

'''@app.route("/simple_chart")
def chart():
    legend = 'Monthly Data'
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = [10, 9, 8, 7, 6, 4, 7, 8]
    return render_template('chart.html', values=values, labels=labels, legend=legend)

@app.route("/chart1")
def chart1():
    labels = ["January","February","March","April","May","June","July","August"]
    values = [10,9,8,7,6,4,7,8]
    return render_template('chart1.html', values=values, labels=labels)'''

if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.permanent_session_lifetime = timedelta(minutes=10)
    app.run(debug=True)
    #app.run(debug=True,host="0.0.0.0")