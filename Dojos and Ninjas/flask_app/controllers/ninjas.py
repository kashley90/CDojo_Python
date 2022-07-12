from flask import render_template,request,redirect
from flask_app import app
from flask_app.models import dojo,ninja

@app.route('/ninjas')
def ninjas():
    return render_template('ninja.html',dojos=dojo.Dojo.everything())

@app.route('create/ninja', methods=['POST'])
def create_ninja():
    ninja.Ninja.file(request.form)
    return redirect('/')