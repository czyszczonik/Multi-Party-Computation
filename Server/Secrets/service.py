from .DBSecretHandler import insertSecret, fetchSecret, fetchSecrets
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask import make_response
import json

def getSecrets():
    username = get_jwt_identity()
    try:
        results = fetchSecrets(username)
        results = json.dumps(results)
        response = make_response(results, 200)
        response.headers['Content-type']= 'application/json'
        return response
    except Exception as e:
        print(e)
        return make_response({"Message": 'Database Error!'} , 500)


@jwt_required
def getSecret(protocolId):
    username = get_jwt_identity()
    try:
        sec = fetchSecret(username, protocolId)
        if sec is None:
            return make_response({"Message": 'Secret not found!'}, 422)
        return make_response(sec.toDictionary(), 200)
    except:
        return make_response({"Message": 'Database Error!'} , 500)


@jwt_required
def createSecret(body):
    username = get_jwt_identity()
    protocolId = body.get("protocolId")
    data = body.get("data")
    try:
        sec = fetchSecret(username, protocolId)
        if sec is not None:
            return make_response({"Message": 'Secret exists'}, 422)
        insertSecret(username, protocolId, data)
        return make_response({"Message": 'Secret Created'}, 201)
    except:
        return make_response({"Message": 'Database Error!'} , 500)

