from flask import Flask, render_template, request, redirect, url_for, session
import dataset
app = Flask(__name__)
# TODO: connect your database here
db=dataset.connect("postgres://fbeumtjfoswdzj:77858ede1315dab822e19dad2a8f5979e76c454512737d9598332c145f8ec4ed@ec2-50-19-89-124.compute-1.amazonaws.com:5432/d9kl1is1chajdc")


@app.route('/',methods=["GET","POST"])
def loginpage():
		if request.method == "GET":
			return render_template('home.html')
		else:
			form = request.form
			username= form["username"]
			password= form["Password"]
			contactsTable = db["Contacts"]

			if len(list(contactsTable.find(username = username, password = password))) == 1:
				return redirect('/home')

			else:
				return render_template('register.html')
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
	feed=db["feed"]
	posts=list(feed.all())[::-1]
	if request.method == "GET":
		return render_template('feed.html',posts=posts)
		
	else:

		form = request.form
		post=form["post"]
		username=form["username"]
		contactsTable = db["Contacts"]
		entry={"username":username,"post":post}
		posts=list(feed.all())[::-1]

		print(username)
		print list(contactsTable.find(username=username))
		if len(list(contactsTable.find(username = username))) >= 1:
			feed.insert(entry)
			return render_template('feed.html',posts=posts)
			print entry
		else:
			return "error"
			return render_template('feed.html',posts=posts)
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











