from flask import Flask, render_template, request, redirect, url_for
import dataset

app = Flask(__name__)
# TODO: connect your database here
db=dataset.connect("postgres://fbeumtjfoswdzj:77858ede1315dab822e19dad2a8f5979e76c454512737d9598332c145f8ec4ed@ec2-50-19-89-124.compute-1.amazonaws.com:5432/d9kl1is1chajdc")

@app.route('/')
@app.route('/home')
def homepage(methods=["POST"]):

	return render_template('home.html')
@app.route('/register')
def register():
	return render_template("register.html")

# TODO: route to /list

# TODO: route to /feed

# TODO: route to /register

# TODO: route to /error

if __name__ == "__main__":
    app.run(port=3000)











