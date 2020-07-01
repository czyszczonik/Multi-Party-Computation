from .DBAuthHandler import getSalt, getUser, createUser, getUserProfile
from .User import User
from .Profile import Profile
from flask import make_response, jsonify, Markup
from flask_jwt_extended import create_access_token
import bcrypt
import datetime

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
    userProfile = getUserProfile(username)
    if user is not None and bcrypt.checkpw(password.encode(), user.password):
        expires = datetime.timedelta(days=365)  
        access_token = create_access_token(identity=username, expires_delta=expires)
        userData = {
            'username': username or '',
            'firstName': userProfile.firstName or '',
            'lastName': userProfile.lastName or '',
            'age': userProfile.age or '',
            'bio': userProfile.bio or '',
            'imageUrl': userProfile.imageUrl or '',
            'phone': userProfile.phone or '',
            'access_token': access_token
        }
        response = make_response(jsonify(userData), 200)
        return response
    return make_response({"Message" : 'Login failed'}, 401)


def register(body):
    username = body.get('username')
    password = body.get('password')
    firstName = Markup.escape(body.get('firstName'))
    lastName = Markup.escape(body.get('lastName'))
    
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


def logout():
    return make_response('', 200)
