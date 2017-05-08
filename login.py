from flask import Flask, redirect, url_for, request, json, Response, abort
#render_template is for render html to your server
from flask import render_template, jsonify

from flask_login import LoginManager, UserMixin, \
                                login_required, login_user, logout_user 

import random
from nocache import nocache
random.seed(1234)

import logging
from logging.handlers import RotatingFileHandler

import os
# sql connector
from flaskext.mysql import MySQL


app = Flask(__name__)

# flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# MySQL configurations
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '1234'
app.config['MYSQL_DATABASE_DB'] = 'lrrs'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

def user_password_check(username, password):
    conn = mysql.connect()
    cursor = conn.cursor()
    query_str = "SELECT password FROM user_pw WHERE username='%s';"%(username)
    cursor.execute(query_str)
    saved_password = cursor.fetchall()
    cursor.close()
    conn.close()
    if saved_password is None or len(saved_password) < 1 or saved_password[0][0]!= password:
        return False
    else:
        return True

# silly user model
class User(UserMixin):

    def __init__(self, id, active=True):
        self.id = id
        self.name = "user" + str(id)
        self.password = self.name + "_password"
        self.active = active
        
    def __repr__(self):
        return "%d/%s/%s" % (self.id, self.name, self.password)

    def is_active(self):
        # Here you should write whatever the code is
        # that checks the database if your user is active
        return self.active

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

# callback to reload the user object        
@login_manager.user_loader
def load_user(userid):
    return User(userid)

@app.route("/")
def root():
    return "Click <a href='/searchpage.html'>here</a> to search rooms."

@app.route("/login", methods=["GET", "POST"])
@nocache
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print('username:password is %s:%s'%(username, password))        
        if user_password_check(username, password):
            id = random.randrange(1,9999)
            user = User(id)
            login_user(user)
            app.logger.info('Info: User %s logged in'%(username))
            return redirect(request.args.get("next"))
        else:
            return abort(401)
    else:
        for arg in request.args:
            print('key:value = %s:%s'%(arg , request.args[arg] ))
        return Response('''
        <!DOCTYPE html>
        <html>
        <head>
        <title>login page</title>
        <h2>Please enter your username and password here:</h2>
        <style type="text/css">
		        h2{
			text-align: left;
			font-size: 24px;
		}

		hr{
			margin-bottom: 30px;
		}

		div.container{
			width: 960px;
			height: 610px;
			margin:50px auto;
			font-family: 'Droid Serif', serif;
			position:relative;
		}

		div.main{
			width: 320px;
			margin-top: 80px;
			float:left;
			padding: 10px 55px 40px;
			background-color: rgba(187, 255, 184, 0.65);
			border: 15px solid white;
			box-shadow: 0 0 10px;
			border-radius: 2px;
			font-size: 13px;
		}

		input[type=text],[type=password] {
			width: 30%;
			height: 34px;
			padding-left: 5px;
			margin-bottom: 20px;
			margin-top: 8px;
			box-shadow: 0 0 5px #00F5FF;
			border: 2px solid #00F5FF;
			color: #4f4f4f;
			font-size: 16px;
		}

		label{
			color: #464646;
			text-shadow: 0 1px 0 #fff;
			font-size: 14px;
			font-weight: bold;
		}

		#login {
			width: 30%;
			background: linear-gradient(#22abe9 5%, #36caf0 100%);
			border: 1px solid #0F799E;
			font-size: 20px;
			margin-top: 15px;
			padding: 8px;
			font-weight: bold;
			cursor: pointer;
			color: white;
			text-shadow: 0px 1px 0px #13506D;
		}

		#login:hover{
		    background: linear-gradient(#36caf0 5%, #22abe9 100%);
		}

		/* -------------------------------------
		    CSS for sidebar (optional) 
		---------------------------------------- */
		.fugo{
			float:right;
		}
        </style>
        </head>	
        <body>
        <br/>
        <form action="" method="post">
            <label for="username">Username:</label>
            <input type="text" name="username"  required="required"><br/>
            <label for="password">Password:</label>
            <input type="password" name="password" required="required"><br/>
            <input type="submit" value="Login">
        </form>
        <body>
        </html>
        ''')


# logout
@app.route("/logout")
@nocache
@login_required
def logout():
    logout_user()
    return Response('<p>You have logged out</p>')


# handle login failed
@app.errorhandler(401)
def page_not_found(e):
    return Response('''
                    <!DOCTYPE html>
                    <html>
                    <head>
                    <style>
                    .alert {
                        padding: 20px;
                        background-color: #f44336;
                        color: white;
                    }

                    .closebtn {
                        margin-left: 15px;
                        color: white;
                        font-weight: bold;
                        float: right;
                        font-size: 22px;
                        line-height: 20px;
                        cursor: pointer;
                        transition: 0.3s;
                    }

                    .closebtn:hover {
                        color: black;
                    }
                    </style>
                    </head>
                    <body>

                    

                    <div class="alert">
                      <span class="closebtn" onclick="this.parentElement.style.display='none';">&times;</span> 
                      <strong>Login failed!</strong> Incorret username or password.
                    </div>

                    <p>Click <a href='/login?next=%2Fsearchpage.html'>here</a> to try again</p>
                    </body>
                    </html>

        ''')
    
    

@app.route('/searchpage.html')
@login_required
@nocache
def searchpage():
    return render_template("searchpage.html")

    
if __name__ == '__main__':
    handler = RotatingFileHandler('log.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.secret_key = os.urandom(12)
    app.run(threaded=True)
