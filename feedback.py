import pymysql

mysql_server="localhost"

class feedback():
    def validateuser(self,**data):
        self.name = data['name']
        self.email = data['email']
        self.eid = data['eid']

        # Open database connection
        db = pymysql.connect(mysql_server, "root", "lokesh1999", "employee")
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


    def insertfeedback(self,**result):
        self.name=result['name']
        self.email= result['email']
        self.eid=result['eid']

        obj=feedback()
        isuser=obj.validateuser(**result)
        if isuser:
            # Open database connection
            db = pymysql.connect(mysql_server, "root", "lokesh1999", "employee")
            # prepare a cursor object using cursor() method
            db.autocommit(False)
            cursor = db.cursor()
            # execute SQL query using execute() method.

            sql = "insert into feedback  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val =(self.eid,int(result['q1']),int(result['q2']),int(result['q3']),int(result['q4']),int(result['q5']),int(result['q6']),
                  int(result['q7']),int(result['q8']),int(result['q9']),int(result['q10']),int(result['q11']),int(result['q12']),int(result['q13']),int(result['q14']),
                    int(result['q15']),int(result['q16']),int(result['q17']),int(result['q18']),int(result['q19']))
            try:
                #print("in try")
                # Execute the SQL command
                cursor.execute(sql,val)
                #print("command executed")
                # Fetch all the rows in a list of lists.
            except Exception as e:
                print(e)
                print("Error: unable to insert data")
                db.close()
                return False
            db.commit()
            db.close()
            return True
        else:
            return False
