from flask import Flask, render_template, request

# TODO: create new Flask app
app = Flask


@app.route("/")
def main_page():
    # TODO: return index.html
    return render_template("index.html")


# TODO: Add route for sign up
@app.route('/sign_up')
def sign_up():
    # TODO: get user input from request
    email = request
    username = request
    password = request

    if not user_exists(email=email, username=username, password=password):
        return "<h2>New user has been created</h2>"
    else:
        return "<h2>This user already exists</h2>"


def user_exists(email, username, password):
    # TODO: check for user if exists, you can use an array as your records.
    if email == "ramy.ashraf2015@gmail.com" and username == "Ramy" and password == "test":

        return True
# Hamada1
