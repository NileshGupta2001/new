'''
!C:/Users/dell/AppData/Local/Programs/Python/Python310/python.exe
'''
print("Content-Type:text/html")
print()

import cgi
print("<h1>Welcome to Python</h1>")
print("<hr/>")
print("<h1>Using input tag</h1>")
print("<body bgcolor='red'>")

form=cgi.FieldStorage()

userid=form.getvalue("userid")
username=form.getvalue("username")
address=form.getvalue("address")
gender=form.getvalue("gender")
hindi=form.getvalue("hindi")
english=form.getvalue("english")
urdu=form.getvalue("urdu")
select1=form.getvalue("select")

#import mysql.connector
import pyodbc
server = 'registerdbnew.database.windows.net'
database = 'try2'
username = 'nilesh'
password = 'uAeSy9@1'   
driver= '{ODBC Driver 17 for SQL Server}'

con=pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
#con=mysql.connector.connect(user='root',password='',host='localhost',database='webpython',port='3307')
cur=con.cursor()

cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s)",(userid,username,address,gender,hindi,english,urdu,select1))
con.commit()

cur.close()
con.close()
print("<h3>YOUR RECORD HAS BEEN SUCCESSFULLY INSERTED!!</h3>")
print("<a href='https://nice-bush-0404bfe10.1.azurestaticapps.net'>GO BACK?</a>")