from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
import re

app = Flask(__name__)

users = {}

errors = {'error':False,'message':''}

@app.route("/", methods=["GET","POST"])
def main_page():
	errors['error'] = False
	if request.method == 'POST':
		if request.form['add_user'] != None:
			pattern = '^[a-zA-Z]+$'
			re_find = re.search(pattern, request.form['add_user'])
			if len(request.form['add_user']) == 0:
				if errors['error'] == False:
					errors['error'] = True
					errors['message'] = 'Error! empty UserName'
			if len(request.form['add_user']) < 6:
				if errors['error'] == False:
					errors['error'] = True
					errors['message'] = 'Error! username is too short'
			if not re_find:
				if errors['error'] == False:
					errors['error'] = True
					errors['message'] = 'Error! username no valid'
			if request.form['add_user'] in users.keys():
				if errors['error'] == False:
					errors['error'] = True
					errors['message'] = 'Error! username is exists'
			if errors['error'] == False:
				users[request.form['add_user']] = {'testest'}
				return render_template("index.html", todos=users)
			else:
				return render_template("index.html", todos=users, errors=errors)
	return render_template("index.html", todos=users)
@app.route("/delete", methods=["POST"])
def deleted():
	users.pop(request.form['delete_name'], None)
	return redirect("/")
@app.route("/<username>", methods=["GET","POST"])
def username(username):
	if request.method == 'GET':
		if username in users.keys():
			return render_template("index.html", usrset=users[username], usrname=username)
		else:
			return redirect("/")
	else:
		if username in users.keys():
			if 'add_task' in request.form:
				users[username].add(request.form['add_task'])
				return render_template("index.html", usrset=users[username], usrname=username)
			elif 'delete_task' in request.form:
				users[username].remove(request.form['delete_task'])
				if len(users[username]) == 0:
					users[username].add('testest')
				return render_template("index.html", usrset=users[username], usrname=username)
if __name__ == '__main__':
	app.run()