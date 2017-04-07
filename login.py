from LRRS.App import app
from LRRS.DBManager.DBHandler import dbHandler
from LRRS.Entities.User import User
import LRRS.lrrs

from flask import render_template
from flask import request
from flask import jsonify

def login():
    return render_template("login.html")


@app.route('/checkuname',methods=['POST'])
def checkuname():

    # read the posted values from the UI
    uname = request.form['username']
    password = request.form['psw']

    oUser = User(uname)
    oUser.set_password(password)

    status = dbHandler.validate_user(oUser)

    return jsonify({'success': status})
    

@app.route('/searchpage.html')
def searchpage():

    return render_template("searchpage.html")



@app.route("/")
def start():
    return login()


if __name__ == '__main__':
   app.run(debug=True)