from flask import Flask, render_template, jsonify, request
from database import load_users_from_db, load_user_from_db, about_from_db, submit_to_db

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


@app.route("/login")
def login_page():
  return render_template('login.html')


# @app.route("/signup")
# def signup_page():
#   return render_template('signup.html')


@app.route("/signup", methods=["POST", "GET"])
def signup_page():
    if request.method == "POST":
        email = request.form["email"]
        selection = request.form.get("selection")
        submit_to_db(email, selection)
        return render_template("signup.html")
    else:
        return render_template("signup.html")  



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
