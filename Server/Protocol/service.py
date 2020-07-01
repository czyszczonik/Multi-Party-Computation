from .DBProtocol import getProtocolByName, getProtocolById, protocolExistis, removeProtocol, putFirstRound, putSecondRound, putThirdRound, putResult, putFourthRound, removeSecrets, getActiveProtocols
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask import make_response
from .Result import Result
import json

@jwt_required
def getActiveProtocolsForUser():
    username = get_jwt_identity()
    try:
        results = getActiveProtocols(username)
        results = json.dumps(results)
        response = make_response(results, 200)
        response.headers['Content-type']= 'application/json'
        return response
    except Exception as e:
        print(e)
        return make_response({"Message": 'Database Error!'} , 500)

@jwt_required
def getProtocolDataById(protocolID):
    username = get_jwt_identity()
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

@jwt_required
def getProtocolDataByName(name):
    username = get_jwt_identity()
    try:
        results = getProtocolByName(username, name)
        results = json.dumps(results)
        if results is "null":
            results = {"status":"false"}
        response = make_response(results, 200)
        response.headers['Content-type']= 'application/json'
        return response
    except Exception as e:
        print(e)
        return make_response({"Message": 'Database Error!'} , 500)

@jwt_required
def initProtocol(body):
    username = get_jwt_identity()
    if body.get("iniciator") != username:
        return make_response({"Message": 'Unauthorized!'} , 401)
    if protocolExistis(username, body.get("responder")):
        return make_response({"Message": 'protocolExistis!'} , 422)
    try:
        putFirstRound(body)
        return make_response({"Message": 'Created Protocol!'} , 201)
    except:
        return make_response({"Message": 'Database Error!'} , 500)


@jwt_required
def respondProtocol(body):
    username = get_jwt_identity()
    id = body.get("protocolId")
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


@jwt_required
def thirdRoundProtocol(body):
    username = get_jwt_identity()
    id = body.get("protocolId")
    if body.get("iniciator") != username:
        return make_response({"Message": 'Unauthorized!'} , 401)
    protocol = getProtocolById(id)
    if not protocol.isTurn(username):
        return make_response({"Message": 'Unauthorized!'} , 401)
    try:
        messagesForResponder = body.get("messagesForResponder")
        putThirdRound(id, messagesForResponder)
        return make_response({"Message": 'Protocol Updated!'} , 204)
    except:
        return make_response({"Message": 'Database Error!'} , 500)

@jwt_required
def fourthRoundProtocol(body):
    username = get_jwt_identity()
    id = body.get("protocolId")
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
    except Exception as e:
        return make_response({"Message": 'Database Error!'} , 500)
