'''
!C:/Users/dell/AppData/Local/Programs/Python/Python310/python.exe
'''
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/connectusingpython2.py')
def my_link():
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

import mysql.connector
#import pyodbc
Server = 'registerdbnew.mysql.database.azure.com'
database = 'register'
username = 'nilesh'
password = 'NewPass@21'   
driver= '{ODBC Driver 17 for SQL Server}'

#con=pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+Server+';DATABASE='+database+';UID='+username+';PWD='+ password)
#con=mysql.connector.connect(user='root',password='',host='localhost',database='webpython',port='3307')
con = mysql.connector.connect(user="nilesh", password="NewPass@21", host="registerdbnew.mysql.database.azure.com", port=3306, database="register", ssl_ca="DigiCertGlobalRootCA.crt", ssl_disabled=False)
cur=con.cursor()

cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s)",(userid,username,address_,gender,hindi,english,urdu,select1))
con.commit()

cur.close()
con.close()
print("<h3>YOUR RECORD HAS BEEN SUCCESSFULLY INSERTED!!</h3>")
print("<a href='https://nice-bush-0404bfe10.1.azurestaticapps.net'>GO BACK?</a>")

if __name__ == '__main__':
  app.run(debug=True)
