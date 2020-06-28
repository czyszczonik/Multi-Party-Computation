from .DBResult import getPairs, getResultsForUser
from flask_login import login_required, current_user
from flask import make_response
import json


@login_required
def getMatchedPairs():
    username = current_user.username
    try:
        results = getResultsForUser(username)
        results = json.dumps(results)
        response = make_response(results, 200)
        response.headers['Content-type']= 'application/json'
        return response
    except:
        return make_response({"Message": 'Database Error!'} , 500)


@login_required
def getUnmatchedPairs():
    username = current_user.username
    try:
        results = getPairs(username)
        results = json.dumps(results)
        response = make_response(results, 200)
        response.headers['Content-type']= 'application/json'
        return response
    except:
        return make_response({"Message": 'Database Error!'} , 500)
