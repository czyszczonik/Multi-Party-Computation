from .DBProfileHandler import getProfileInfo, updateProfileInfo
from flask_login import login_required, current_user
from flask import make_response

@login_required
def getProfile():
    username = current_user.username
    try:
        response = getProfileInfo(username).toDictionary()
        return make_response(response, 200)
    except:
        return make_response('', 500)

@login_required
def updateProfile(body):    
    username = current_user.username
    profile = getProfileInfo(username)    
    imageUrl = body.get("imageUrl") or profile.imageUrl
    age = body.get("age") or profile.age
    bio = body.get("bio") or profile.bio
    phone = body.get("phone") or profile.phone
    try:
        updateProfileInfo(username, "imageUrl", imageUrl)
        updateProfileInfo(username, "age", age)
        updateProfileInfo(username, "bio", bio)
        updateProfileInfo(username, "phone", phone)
        return make_response("Updated", 200)
    except:
        return make_response('', 500)
