from flask import Flask, session, render_template, url_for, redirect, request
from forms import RegistrationForm, roomRegistration, loginRegistration
import numpy as np
import ssl

app = Flask(__name__)
 
#CSRF(Cross-Site Request Forgery)
app.config["SECRET_KEY"] = 'd2707fea9778e085491e2dbbc73ff30e'

@app.route('/', methods=["GET","POST"])
def login():
    session.pop('login_user', None)
    if request.method == 'POST':
        session['login_user'] = request.form['id']
        return redirect(url_for('main'))
    return render_template("login.html")

@app.route('/register', methods=["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        return render_template("getimg.html")
    return render_template("register.html", form=form)

@app.route('/register/getImg')
def getcapture():
    return render_template("getimg.html")    
    
@app.route('/register/character', methods=["GET","POST"])
def character():
    return render_template("character.html")

@app.route('/main', methods=["GET","POST"])
def main():
    return render_template("main.html")

@app.route('/newroom',methods=["GET","POST"])
def newroom():
    form = roomRegistration()
    if form.validate_on_submit():
        roomname=request.form["className"]
        return render_template("roomInfo.html",roomName=roomname,roomNum="예시클래스번호")
    return render_template("newroom.html",form=form)

@app.route('/newroom/roomInfo', methods=["GET","POST"])
def roomInfo():
    roomname="클래스이름예시"
    roomAddress="클래스번호예시"
    return render_template("roomInfo.html",roomName=roomname,roomNum=roomAddress)

@app.route('/enter',methods=["GET","POST"])
def enter():
    if request.method == 'POST':
        roomNum=request.form['classNum']
        return redirect(url_for('room',room_id=roomNum))
    return render_template("enter.html")

@app.route('/<int:room_id>',methods=["GET","POST"])
def room(room_id):
    return render_template("room.html", room_id=room_id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443, debug=True, ssl_context='adhoc')