from flask import Flask, render_template, request, redirect, url_for, session
import dataset
import os

app = Flask(__name__)
# TODO: connect your database here
db=dataset.connect("postgres://fbeumtjfoswdzj:77858ede1315dab822e19dad2a8f5979e76c454512737d9598332c145f8ec4ed@ec2-50-19-89-124.compute-1.amazonaws.com:5432/d9kl1is1chajdc")
app.secret_key='\xc35\xd8fT\xa3\xc90\xe5<\xa7!\xef\xaa\x1atV\xc1\d07\xe8\xa7\xbeQt\xb6'
@app.route('/logout')
def logout():
	session.pop("username",None)
	return redirect('/login')

@app.route('/',methods=["GET","POST"])
@app.route('/login',methods=["GET","POST"])
def loginpage():
		if request.method == "GET":
			return render_template('home.html')
		else:
			form = request.form
			username= form["username"]
			password= form["Password"]
			contactsTable = db["Contacts"]

			if len(list(contactsTable.find(username = username, password = password))) == 1:
				session["username"] = username
				return redirect('/feed')

			else:
				return redirect('/login')
				print"YES"

@app.route('/home',methods=["GET","POST"])
def home():
	return redirect('/feed')

@app.route('/register',methods=["POST","GET"])
def register():

	if request.method == "GET":
		return render_template('register.html')
	else:
		form = request.form
		email= form["email"]
		password= form["Password"]
		firstname= form["First name"]
		lastname = form["Last name"]
		username = form["User name"]
		country = form["Country"]
		contactsTable = db["Contacts"]
		entry = {"email":email, "password":password, "firstname":firstname, "lastname":lastname, "username":username, "country":country}
		#students names to check
		if len(list(contactsTable.find(username = username))) == 0:
			contactsTable.insert(entry)
			print list(contactsTable.all())
			return render_template('home.html')

		else:
			print"YES"
			return render_template('home.html')
	
@app.route('/list',methods=["POST","GET"])
def list_users():
	contactsTable = db["Contacts"]
	allcontacts = list(contactsTable.all())
	return render_template('list.html' ,contacts=allcontacts)


@app.route('/feed',methods=["POST","GET"])
def feed():
	# session["username"] = username
	if "username" in session: 
		feed=db["feed"]
		posts=list(feed.all())[::-1]
		c_user = session["username"]
		if request.method == "GET":
			return render_template('feed.html',posts=posts,c_user=c_user)
			
		else:

			form = request.form
			post=form["post"]
			contactsTable = db["Contacts"]
			entry={"username":c_user,"post":post}
			posts=list(feed.all())[::-1]

			print(c_user)
			print list(contactsTable.find(username=c_user))
			if len(list(contactsTable.find(username = c_user))) >= 1:
				feed.insert(entry)
				posts=list(feed.all())[::-1]
				return render_template('feed.html',posts=posts,c_user=c_user)
				print entry
			else:
				return redirect('/login')
			# else:
			# 	return "error"
			# 	return render_template('feed.html',posts=posts,c_user=c_user)
	else:
		return redirect('/login')
@app.route('/wecode')
def wecode():
	return render_template('wecode.html')

	# contactsTable = db["Contacts"]
	# allcontacts = list(contactsTable.all())
	# return render_template('feed.html' ,contacts=allcontacts)	
# TODO: route to /list

# TODO: route to /feed

# TODO: route to /register

# TODO: route to /error

if __name__ == "__main__":
    app.run(port=3000)











