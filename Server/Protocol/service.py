from .DBProtocol import getProtocolByName, getProtocolById, protocolExistis, removeProtocol, putFirstRound, putSecondRound, putThirdRound, putResult, putFourthRound, removeSecrets, getActiveProtocols
from flask_login import login_required, current_user
from flask import make_response
from .Result import Result
import json


def getActiveProtocolsForUser():
    username = current_user.username
    try:
        results = getActiveProtocols(username)
        results = json.dumps(results)
        response = make_response(results, 200)
        response.headers['Content-type']= 'application/json'
        return response
    except:
        return make_response({"Message": 'Database Error!'} , 500)


def getProtocolDataById(protocolID):
    username = current_user.username
    try:
        results = getProtocolById(protocolID)
        if result.iniciator != username and result.responder != username:
            return make_response({"Message": 'Unauthorized!'} , 401)
        results = json.dumps(results)
        response = make_response(results, 200)
        response.headers['Content-type']= 'application/json'
        return response
    except:
        return make_response({"Message": 'Unauthorized!'} , 401)


def getProtocolDataByName(name):
    username = current_user.username
    try:
        results = getProtocolByName(username, name)
        results = json.dumps(results)
        response = make_response(results, 200)
        response.headers['Content-type']= 'application/json'
        return response
    except:
        return make_response({"Message": 'Database Error!'} , 500)


def initProtocol(body):
    username = current_user.username
    if body.get("iniciator") != username:
        return make_response({"Message": 'Unauthorized!'} , 401)
    if protocolExistis(username, body.get("responder")):
        return make_response({"Message": 'protocolExistis!'} , 422)
    try:
        putFirstRound(body)
        return make_response({"Message": 'Created Protocol!'} , 201)
    except:
        return make_response({"Message": 'Database Error!'} , 500)



def respondProtocol(body):
    username = current_user.username
    id = body.get("protocolID")
    if body.get("responder") != username:
        return make_response({"Message": 'Unauthorized!'} , 401)
    protocol = getProtocolById(id)
    if not protocol.isTurn(username):
        return make_response({"Message": 'Unauthorized!'} , 401)
    try:
        v = body.get("v")
        putSecondRound(id, v)
        return make_response({"Message": 'Protocol Updated!'} , 204)
    except:
        return make_response({"Message": 'Database Error!'} , 500)



def thirdRoundProtocol(body):
    username = current_user.username
    id = body.get("protocolID")
    if body.get("iniciator") != username:
        return make_response({"Message": 'Unauthorized!'} , 401)
    protocol = getProtocolById(id)
    if not protocol.isTurn(username):
        return make_response({"Message": 'Unauthorized!'} , 401)
    try:
        iniciatorChecks = body.get("iniciatorChecks")
        putThirdRound(id, iniciatorChecks)
        return make_response({"Message": 'Protocol Updated!'} , 204)
    except:
        return make_response({"Message": 'Database Error!'} , 500)


def fourthRoundProtocol(body):
    username = current_user.username
    id = body.get("protocolID")
    if body.get("responder") != username:
        return make_response({"Message": 'Unauthorized!'} , 401)
    protocol = getProtocolById(id)
    if not protocol.isTurn(username):
        return make_response({"Message": 'Unauthorized!'} , 401)
    try:
        responderLabels = body.get("responderLabels")
        putFourthRound(id, responderLabels)
        proto = getProtocolById(id)
        putResult(proto.iniciator, proto.responder, proto.computeResult())
        removeProtocol(id)
        removeSecrets(id)
        return make_response({"Message": 'Protocol Updated!'} , 204)
    except:
        return make_response({"Message": 'Database Error!'} , 500)
