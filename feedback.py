import pymysql
from ChurnPred import churn
mysql_server="localhost"
password="lokesh1999"
class feedback():
    def predictChurn(self,satisfaction):
        obj = churn()
        churn_pred=obj.gb.predict()
        return True

    def validateuser(self,**data):
        self.name = data['name']
        self.email = data['email']
        self.eid = data['eid']

        # Open database connection
        db = pymysql.connect(mysql_server, "root", password, "employee")
        # prepare a cursor object using cursor() method
        db.autocommit(False)
        cursor = db.cursor()

        # execute SQL query using execute() method.
        val= (self.eid,self.email)

        try:

            # Execute the SQL command
            cursor.execute("SELECT email from users where id=%s",(self.eid))

            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
            emailid=results[0][0]
        except:
            print("Error: unable to fetch data")
            db.commit()
            db.close()
            return False
        if emailid == self.email:
            db.commit()
            db.close()
            return True
        else:
            db.commit()
            db.close()
            return False

    def isfeedback(self,**data):
        self.name = data['name']
        self.email = data['email']
        self.eid = data['eid']

        # Open database connection
        db = pymysql.connect(mysql_server, "root", password, "employee")
        # prepare a cursor object using cursor() method
        db.autocommit(False)
        cursor = db.cursor()

        # execute SQL query using execute() method.
        val = (self.eid, self.email)

        try:

            # Execute the SQL command
            cursor.execute("SELECT id from feedback where id=%s", (self.eid))

            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
            id = results[0][0]
        except:
            print("Error: unable to fetch data1")
            db.commit()
            db.close()
            return False
        if int(id) == int(self.eid):
            db.commit()
            db.close()
            return True
        else:
            db.commit()
            db.close()
            return False


    def insertfeedback(self,**result):
        self.name=result['name']
        self.email= result['email']
        self.eid=result['eid']

        obj=feedback()
        isuser=obj.validateuser(**result)
        isfeed = obj.isfeedback(**result)
        satisfaction = int(result['q1'])*0.03+int(result['q2'])*0.03\
                        +int(result['q3'])*0.005+int(result['q4'])*0.005+int(result['q5'])*0.005+int(result['q6'])*0.005\
                        +int(result['q7'])*0.01+int(result['q8'])*0.01\
                        +int(result['q9'])*0.0066+int(result['q10'])*0.0066+int(result['q11'])*0.0068\
                        +int(result['q12'])*0.01+int(result['q13'])*0.01\
                        +int(result['q14'])*0.0066+int(result['q15'])*0.0066+int(result['q16'])*0.0068\
                        +int(result['q17'])*0.0132+int(result['q18'])*0.0132+int(result['q19'])*0.0136
        print(isfeed)
        if isuser:
            # Open database connection
            db = pymysql.connect(mysql_server, "root", password, "employee")
            # prepare a cursor object using cursor() method
            db.autocommit(False)
            cursor = db.cursor()
            # execute SQL query using execute() method.
            if isfeed:
                sql = "UPDATE feedback SET q1=%s,q2=%s,q3=%s,q4=%s,q5=%s,q6=%s,q7=%s,q8=%s,q9=%s,q10=%s,q11=%s,q12=%s,q13=%s,q14=%s,q15=%s,q16=%s,q17=%s,q18=%s,q19=%s WHERE id=%s"
                val = (
                    int(result['q1']), int(result['q2']), int(result['q3']), int(result['q4']),
                    int(result['q5']),
                    int(result['q6']),
                    int(result['q7']), int(result['q8']), int(result['q9']), int(result['q10']), int(result['q11']),
                    int(result['q12']), int(result['q13']), int(result['q14']),
                    int(result['q15']), int(result['q16']), int(result['q17']), int(result['q18']), int(result['q19']),self.eid)
                try:
                    # print("in try")
                    # Execute the SQL command
                    cursor.execute(sql, val)
                    # print("command executed")
                    # Fetch all the rows in a list of lists.
                except Exception as e:
                    print(e)
                    print("Error: unable to replace data")
                    db.close()
                    return False



                sql = "UPDATE users SET satisfaction=%s,churn=%s where id=%s"
                val = (2, 0, self.eid)

                try:
                    # print("in try")
                    # Execute the SQL command
                    cursor.execute(sql, val)
                    # print("command executed")
                    # Fetch all the rows in a list of lists.
                except Exception as e:
                    print(e)
                    print("Error: unable to replace data")
                    db.close()
                    return False
                db.commit()
                db.close()
                return True
            else:
                print("in inserting feedback")
                sql = "insert into feedback  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val = (
                self.eid, int(result['q1']), int(result['q2']), int(result['q3']), int(result['q4']), int(result['q5']),
                int(result['q6']),
                int(result['q7']), int(result['q8']), int(result['q9']), int(result['q10']), int(result['q11']),
                int(result['q12']), int(result['q13']), int(result['q14']),
                int(result['q15']), int(result['q16']), int(result['q17']), int(result['q18']), int(result['q19']))
                try:
                    # print("in try")
                    # Execute the SQL command
                    cursor.execute(sql, val)
                    # print("command executed")
                    # Fetch all the rows in a list of lists.
                except Exception as e:
                    print(e)
                    print("Error: unable to insert data")
                    db.close()
                    return False


                sql = "UPDATE users SET satisfaction=%s,churn=%s where id=%s"
                val = (satisfaction, 0,int(self.eid))
                print("going to replace in users")
                try:
                    # print("in try")
                    # Execute the SQL command
                    cursor.execute(sql, val)
                    # print("command executed")
                    # Fetch all the rows in a list of lists.
                except Exception as e:
                    print(e)
                    print("Error: unable to replace data")
                    db.close()
                    return False
                print("replaced")
                db.commit()
                db.close()
                return True
        else:
            return False

