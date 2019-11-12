#import modules
import matplotlib
import pandas as pd # for dataframes
import matplotlib.pyplot as plt # for plotting graphs
#import seaborn as sns # for plotting graphs
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
import numpy as np
class churn:
    data = pd.read_csv('HR_comma_sep.csv')
    left = data.groupby('left')
    #print(left.mean())
    satisfaction_level=pd.crosstab(data.satisfaction_level,data.left)
    bins = np.arange(0, 1.1, 0.2)
    ind = np.digitize(satisfaction_level.index, bins)

    satisfaction_level = satisfaction_level.groupby(ind).sum()
    satisfaction_level.index = np.array(bins)
    #print(satisfaction_level)
    satisfaction_level[[0, 1]] = satisfaction_level[[0, 1]].apply(lambda x: x / x.sum() * 100, axis=1)

    sal = pd.crosstab(data.salary, data.left, normalize='index').round(4) * 100
    sal=sal.sort_values(0,ascending=False)
    prom = pd.crosstab(data.promotion_last_5years, data.left, normalize='index').round(4) * 100
    Dep = pd.crosstab(data.Departments, data.left, normalize='index').round(4) * 100
    Dep=Dep.sort_values(by=[1])
    #print(Dep)
    left_count=data.left.value_counts()
    # creating labelEncoder
    le = preprocessing.LabelEncoder()
    # Converting string labels into numbers.
    data['salary'] = le.fit_transform(data['salary'])
    data['Departments'] = le.fit_transform(data['Departments'])
    # Spliting data into Feature and
    X = data[['satisfaction_level', 'last_evaluation', 'number_project',
              'average_montly_hours', 'time_spend_company', 'Work_accident',
              'promotion_last_5years', 'Departments', 'salary']]
    y = data['left']
    # Split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,random_state=42)  # 70% training and 30% test
    # Create Gradient Boosting Classifier
    gb = GradientBoostingClassifier()

    # Train the model using the training sets
    gb.fit(X_train, y_train)

    # Predict the response for test dataset
    y_pred = gb.predict(X_test)
    y_pred = pd.DataFrame(y_pred)
    pred_count=y_pred[0].value_counts()