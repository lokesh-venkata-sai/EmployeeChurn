import pymysql
mysql_server="localhost"
password="lokesh1999"
class Employee():
    def getEmployeeList(self):
        db = pymysql.connect(mysql_server, "root", password, "employee")
        cursor = db.cursor()

        try:
            # Execute the SQL command

            cursor.execute("SELECT * from users")
            # Fetch all the rows in a list of lists.
            users = cursor.fetchall()
        except:
            print("Error: unable to fetch data")
        db.close()
        if users:
            #print(users)
            return users
        else:
            return False