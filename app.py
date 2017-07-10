import pypyodbc
from flask import Flask, render_template, json ,request

app = Flask(__name__)
connection=pypyodbc.connect('DRIVER={SQL Server};SERVER=KAIF-PC\MSSQL;DATABASE=BucketList;Trusted_Connection=True;')
cursor = connection.cursor()
cursor.execute("SELECT * FROM tb_user")
s="<table style='border:1px solid red'>"
for row in cursor:
    s=s + "<tr>"
for x in row:
    s=s + "<td>" + str(x) + "</td>"
s=s + "</tr>"

connection.close()
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/test')
def test():
    return  render_template('test.html')

@app.route('/showSignUp')
def showSignUp():
    return  render_template('signup.html')
@app.route('/app')
def APP():
    return '<h1>Hello World!</h1>'

@app.route('/Data')
def Data():
    return "<html><body>" + s + "</body></html>"


if __name__ == "__main__":
    app.run(debug=True)