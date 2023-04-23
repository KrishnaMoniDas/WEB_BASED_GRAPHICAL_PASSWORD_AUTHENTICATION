from flask import Flask, render_template, jsonify, request, redirect, url_for

from database import load_users_from_db, load_user_from_db, about_from_db, submit_to_db, valid_login

app = Flask(__name__)

MEMBERS = [{
  'id': 1,
  'name': 'Krishna Moni Das'
}, {
  'id': 2,
  'name': 'Milonjyoti Borah'
}, {
  'id': 3,
  'name': 'Abir Banerjee'
}, {
  'id': 4,
  'name': 'Amarjeet Boruah'
}]
  

@app.route("/")
def hello_world():
  users = load_users_from_db()
  about = about_from_db()
  return render_template('home.html',
                         Website_dev='Krishna Moni Das',
                         users=users,
                         members=MEMBERS, about=about)


@app.route("/login", methods=["POST", "GET"])
def login_page():
  if request.method == "POST":
        email = request.form["login_email"]
        selection = request.form.get("login_selection")
        result = valid_login(email, selection)
        print(result)
        if result == 1:
          return redirect(url_for('login_success')) #successfully loggedin
        else:
          return redirect(url_for('login_failed'))
  else:
    return render_template("login.html")




@app.route("/signup", methods=["POST", "GET"])
def signup_page():
    if request.method == "POST":
        email = request.form["email"]
        selection = request.form.get("selection")
        result = submit_to_db(email, selection)
        if result == 1:
          return redirect(url_for('success')) #successfully signedup
        else:
          return redirect(url_for('signup_failed'))
    else:
        return render_template("signup.html") 


@app.route("/success")
def success():
  return render_template("response.html")


@app.route("/signup_failed")
def signup_failed():
  return render_template("problem_signing_up.html")


@app.route("/login_success")
def login_success():
  return render_template("response_login.html")


@app.route("/login_failed")
def login_failed():
  return render_template("user_doesnt_exist.html")



@app.route("/users/<id>")
def showuser(id):
  user = load_user_from_db(id)
  return render_template('userpage.html',user=user)


@app.route("/users")
def allusers():
  users = load_users_from_db()
  return jsonify(users)



if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
