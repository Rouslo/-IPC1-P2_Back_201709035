  
from flask import Flask, render_template, request, redirect, url_for, flash, current_app
import json
name=""
contraseña=""
app = Flask(__name__)

@app.route('/')
def main_page():
    current_app.logger.info('Mostrando los posts del blog')
    
    return None


@app.route('/inicio.html',methods=["GET", "POST"])
def add_contact():
    if request.method=='POST':
        name=request.form['name']
        contraseña=request.form['contraseña']
        print(name)
        print(contraseña)
             
        #return render_template('index.html')
        
        

if __name__ == '__main__':
     app.run()
        

