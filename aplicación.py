from flask import Flask, render_template, session, request, redirect, url_for,flash
from modelo import *

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'hardware+10'
app.config['MYSQL_DB'] = 'flaskdb'

 infraestructura=Infraestructura(app)

app.secret_key='mysecretkey'

@app.route('/')
def home():
    return redirect(url_for('login'))
    
@app.route('/login')
def login():
    session['estado']=False
    return render_template("login.html")
@app.route('/error',methods=["GET","POST"])
def ingreso():
    if infraestructura.existencia_login(request.form['cui'],request.form['password']):
        session['estado']=True
        return  "Acceso permitido, buenos dias"
    else:
        return "Error password and CUI not match"
if __name__=='__main__':#si el archivo que se esta ejecutando es el main es decir el app.py entonces arranca el servidor
    app.run(port=3000,debug=True)#corre el servidor
