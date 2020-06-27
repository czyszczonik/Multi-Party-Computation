import json

class Secret():
    def __init__(self, username, protocolId = None, data = None):
        if protocolId is None:
            json_data = username
            self.username = json_data['username']
            self.protocolId = json_data['protocolId']
            self.data = json_data['data']
        else:
            self.username = username
            self.protocolId = protocolId
            self.data = data


    def toDictionary(self):
        return self.__dict__

    def __str__(self):
        return f"Username: [{self.username}], protocolId: [{self.protocolId}], data: [{self.data}]"
