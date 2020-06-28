from .DBAuthHandler import getSalt, getUser, createUser
from .User import User
from .Profile import Profile
from flask import make_response
from flask_login import login_required, login_user, current_user, logout_user
import bcrypt

def salt(username):
    salt = getSalt(username)
    if salt is None:
        return make_response({"Message" : f"Salt for {username} not found!"}, 422)
    responseBody = {'salt':salt}
    return make_response(responseBody, 200)

def login(body):
    username = body.get('username')
    password = body.get('password')
    user = getUser(username)
    if user is not None and bcrypt.checkpw(password.encode(), user.password):
        login_user(user, remember=True)
        return make_response({"Logged" : f"{username}"}, 200)
    return make_response({"Message" : 'Login failed'}, 401)


def register(body):
    username = body.get('username')
    password = body.get('password')
    firstName = body.get('firstName')
    lastName = body.get('lastName')
    
    salt = body.get('salt')
    if getUser(username).username is not None:
        return make_response({"Message" : 'Username already in use'}, 400)

    # Password hashing
    passwordSalt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), passwordSalt)
    user = {"username" : username,
            "password" : hashed,
            "salt" : salt}

    createUser(User(user), Profile(username, firstName, lastName))

    return make_response({"Message" : 'Registration successful'}, 200)


@login_required
def logout():
    logout_user()
    return make_response('', 200)
