from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/')
def info():
    return redirect('/dojos')


@app.route('/dojos')
def dojos():
    dojos=Dojo.everything()#selecting all dojos
    return render_template("info.html",all_dojos=dojos)

@app.route('/create/dojo', methods=['post'])
def new_dojo():
    Dojo.file(request.form)#keeping information!
    return redirect('/dojos')

@app.route('/dojo/<int:id>')
def dojoshow(id):
    data={
        "id":id
    }
    return render_template('dojo.html',dojo=Dojo.with_ninjas(data))