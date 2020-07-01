from .DBResult import getPairs, getResultsForUser
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask import make_response
import json
import time


@jwt_required
def getMatchedPairs():
    username = get_jwt_identity()
    try:
        results = getResultsForUser(username)
        results = json.dumps(results)
        response = make_response(results, 200)
        response.headers['Content-type']= 'application/json'
        return response
    except:
        return make_response({"Message": 'Database Error!'} , 500)


@jwt_required
def getUnmatchedPairs():
    username = get_jwt_identity()
    try:
        results = getPairs(username) #username, last name, first name, age, bio
        results = json.dumps(results)
        response = make_response(results, 200)
        response.headers['Content-type']= 'application/json'
        return response
    except:
        return make_response({"Message": 'Database Error!'} , 500)
