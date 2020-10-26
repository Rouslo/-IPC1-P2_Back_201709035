  
from flask import Flask, render_template, request, redirect, url_for, flash, current_app
from flask import Markup 
name=""
contraseña=""
app = Flask(__name__)
global cliente
cliente=[]
usu="admin"
ape="Maestro"
nom="Usuario"
contra="admin"


@app.route('/')
def main_page():
    cliente.append(["Usuario","Maestro","admin","admin"])
    return render_template('admo.html')

@app.route('/insertar',methods=["GET", "POST"])
def add_contact():
    estado=False
    if request.method=='POST':
        a=request.form['u1']
        b=request.form['u2']
        c=request.form['u3']
        d=request.form['p1']
        for i in range(len(cliente)):
            if cliente[i][2]==str(c):
                estado=True

        if(estado==False):
            cliente.append([str(a),str(b),str(c),str(d)])
            flash("REGISTRADO") 
            return render_template('principal.html') 
        else:
            flash("REGISTRO YA EXISTE") 
            return render_template('registro.html')


@app.route('/leer',methods=["GET", "POST"])
def ver_login():
    estado=False
    if request.method=='POST':
        a=request.form['u1']
        b=request.form['p1']
        for i in range(len(cliente)):
            if cliente[i][2]==a and cliente[i][3]==b:
                estado=True
        if(a==usu and b==contra):
            flash("BIENVENIDO ADMO") 
            return render_template('principal.html')
        
        else:
            if(estado==False):
                flash("USUARIO NO EXISTE") 
                return render_template('principal.html') 
            else:
                flash("BIENVENIDO") 
                return render_template('login.html') 

@app.route('/recuperar',methods=["GET", "POST"])
def recuperar():
    if request.method=='POST':
        a=request.form['u1']
        for i in range(len(cliente)):
            if cliente[i][2]==a:
                flash("su contraseña es: "+cliente[i][3]) 
                return render_template('login.html') 
 
            else:
                flash("USUARIO NO EXISTE") 
                return render_template('principal.html') 
        






@app.route('/ir_registro',methods=["GET", "POST"])
def ir_registro():
    if request.method=='POST':
        return render_template('registro.html') 

@app.route('/ir_login',methods=["GET", "POST"])
def ir_login():
    if request.method=='POST':
        return render_template('login.html') 

@app.route('/ir_recuperar',methods=["GET", "POST"])
def ir_recuperar():
    if request.method=='POST':
        return render_template('recuperar.html') 
    

if __name__ == '__main__':
    app.secret_key = 'super secret key' 
    app.config['SESSION_TYPE'] = 'filesystem' 
    app.run()
        



