from flask import Flask, render_template, request, redirect, url_for
import dataset

app = Flask(__name__)
# TODO: connect your database here
db=dataset.connect("postgres://fbeumtjfoswdzj:77858ede1315dab822e19dad2a8f5979e76c454512737d9598332c145f8ec4ed@ec2-50-19-89-124.compute-1.amazonaws.com:5432/d9kl1is1chajdc")


@app.route('/',methods=["GET","POST"])
@app.route('/home',methods=["GET","POST"])
def homepage():
		if request.method == "GET":
			return render_template('home.html')
		else:
			form = request.form
			username= form["username"]
			password= form["Password"]
			contactsTable = db["Contacts"]

			if len(list(contactsTable.find(username = username, password = password))) == 1:
				return render_template('register.html')

			else:
				print"YES"
				return render_template('home.html')


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
	

# TODO: route to /list

# TODO: route to /feed

# TODO: route to /register

# TODO: route to /error

if __name__ == "__main__":
    app.run(port=3000)











