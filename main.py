from datetime import timedelta
from flask import Markup
from flask import Flask, request, render_template, url_for, session, redirect, g, jsonify
import os
import pymysql
from flask_googlecharts import GoogleCharts, MaterialLineChart, PieChart, Histogram
from flask_googlecharts import BarChart
from flask_googlecharts.utils import prep_data
import datetime
from ChurnPred import churn
import numpy as np
from Employees import Employee
from feedback import feedback
app = Flask(__name__)
charts = GoogleCharts()
charts.init_app(app)

mysql_server="localhost"
# app.config.from_pyfile("config.cfg")


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
    obj=churn()
    satisfaction_level = obj.satisfaction_level
    sat_left = np.array(satisfaction_level[1])
    list = []
    for i in range(len(satisfaction_level.index.values)):
        list1 = [str(satisfaction_level.index.values[i]), int(sat_left[i])]
        list.append(list1)
    hist = Histogram("hist",
                     options={"title": "Satisfaction_level Vs Left",
                              "width": 500,
                              "height": 300})
    hist.add_column("string", "Satisfcation")
    hist.add_column("number", "#left")
    hist.add_rows(list)
    charts.register(hist)
    return render_template("GoogleChart.html")

@app.route('/')
def index():
    obj = churn()
    train_left_count = obj.left_count[1]
    train_notleft_count = obj.left_count[0]
    test_left_count = obj.pred_count[1]
    test_notleft_count = obj.pred_count[0]
    hot_dog_chart = BarChart("hot_dogs", options={"title": "Employee Churn",
                                                  "width": 500,
                                                  "height": 300})
    hot_dog_chart.add_column("string", "Employee Status")
    hot_dog_chart.add_column("number", "No.of Employees")
    hot_dog_chart.add_rows([["left",int(train_left_count)],
                            ["Not left",int(train_notleft_count)]])
    charts.register(hot_dog_chart)
    spectators_chart = MaterialLineChart("spectators",
                                         options={"title": "Contest Spectators",
                                                  "width": 500,
                                                  "height": 300},
                                         data_url=url_for('data'))

    charts.register(spectators_chart)

    pie_chart= PieChart("pie_chart",options={"title":"Employee Churn",
                                        "width":500,
                                        "height":300})
    pie_chart.add_column("string","Employee Status")
    pie_chart.add_column("number","Number")
    pie_chart.add_rows([["left",int(train_left_count)],
                        ["Not left",int(train_notleft_count)]])
    charts.register(pie_chart)
    #-------------------For predicted-----------------
    hot_dog_chart1 = BarChart("hot_dogs1", options={"title": "Employee Churn",
                                                  "width": 500,
                                                  "height": 300})
    hot_dog_chart1.add_column("string", "Employee Status")
    hot_dog_chart1.add_column("number", "No.of Employees")
    hot_dog_chart1.add_rows([["left", int(test_left_count)],
                            ["Not left", int(test_notleft_count)]])
    charts.register(hot_dog_chart1)
    pie_chart1 = PieChart("pie_chart1", options={"title": "Employee Churn",
                                               "width": 500,
                                               "height": 300})
    pie_chart1.add_column("string", "Employee Status")
    pie_chart1.add_column("number", "Number")
    pie_chart1.add_rows([["left", int(test_left_count)],
                        ["Not left", int(test_notleft_count)]])
    charts.register(pie_chart1)


    satisfaction_level=obj.satisfaction_level
    sat_left=np.array(satisfaction_level[1])
    satisfaction_chart1 = MaterialLineChart("satisfaction_chart1",
                                         options={"title": "Satisfaction_level Vs Left",
                                                  "width": 1000,
                                                  "height": 300})

    satisfaction_chart1.add_column("string", "Satisfcation")
    satisfaction_chart1.add_column("number", "Percentage left")
    list=[]
    for i in range(len(satisfaction_level.index.values)):
        list1 = [str(satisfaction_level.index.values[i]), int(sat_left[i])]
        list.append(list1)
    satisfaction_chart1.add_rows(list)
    charts.register(satisfaction_chart1)

    sal_chart=MaterialLineChart("sal_chart",
                                options={"title":"Salary Vs Left",
                                         "width":500,
                                         "height":300})
    sal=obj.sal
    sal_val=[]
    for i in range(len(sal.index.values)):
        listi=[str(sal.index.values[i]),int(sal[1][i])]
        sal_val.append(listi)

    sal_chart.add_column("string","Salary")
    sal_chart.add_column("number","Percentage Left")
    sal_chart.add_rows(sal_val)
    charts.register(sal_chart)

    prom_chart = BarChart("prom_chart",
                                  options={"title": "Promotion in last 5 years Vs Left",
                                           "width": 500,
                                           "height": 300})
    prom = obj.prom
    prom_val = []
    for i in range(len(prom.index.values)):
        listp = [str(prom.index.values[i]), int(prom[1][i])]
        prom_val.append(listp)

    prom_chart.add_column("string", "Promotion last 5 years")
    prom_chart.add_column("number", "Percentage Left")
    prom_chart.add_rows(prom_val)
    charts.register(prom_chart)

    dep_chart = BarChart("dep_chart",
                          options={"title": "Department Vs Left",
                                   "width": 500,
                                   "height": 300})
    dep = obj.Dep
    dep_val = []
    for i in range(len(dep.index.values)):
        listd = [str(dep.index.values[i]), int(dep[1][i])]
        dep_val.append(listd)

    dep_chart.add_column("string", "Department")
    dep_chart.add_column("number", "Percentage Left")
    dep_chart.add_rows(dep_val)
    charts.register(dep_chart)
    return render_template("index.html")


@app.route('/EmployeeSatisfaction.html')
def employeeform():
    return render_template("EmployeeSatisfaction.html")


@app.route('/EmployeeList.html')
def employeelist():
    obj=Employee()
    users=obj.getEmployeeList()
    if users==False:
        return render_template("EmployeeList.html",users=False)
    else:
        return render_template("EmployeeList.html", users=users)


@app.route('/Form', methods=['GET', 'POST'])
def Form():
    result = request.form
    #print(result)
    obj=feedback()
    ans=obj.insertfeedback(**result)

    if ans == True:
        return render_template("EmployeeSatisfaction.html", post=True)
    else:
        return render_template("EmployeeSatisfaction.html", post=False)

if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.permanent_session_lifetime = timedelta(minutes=10)
    app.run(debug=True)
    #app.run(debug=True,host="0.0.0.0")