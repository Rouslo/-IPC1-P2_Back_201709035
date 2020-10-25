  
from flask import Flask, render_template, request, redirect, url_for, flash, current_app
from flask import Markup 
name=""
contraseña=""
app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('principal.html')

@app.route('/insertar',methods=["GET", "POST"])
def add_contact():
    if request.method=='POST':
        name=request.form['u1']
        contraseña=request.form['u2']
        print(name)
        print(contraseña)
       
        flash("REGISTRADO") 
        return render_template('registro.html') 

@app.route('/ir_registro',methods=["GET", "POST"])
def ir_registro():
    if request.method=='POST':
        return render_template('registro.html') 

@app.route('/ir_login',methods=["GET", "POST"])
def ir_login():
    if request.method=='POST':
        return render_template('login.html') 
    

if __name__ == '__main__':
    app.secret_key = 'super secret key' 
    app.config['SESSION_TYPE'] = 'filesystem' 
    app.run()
        

