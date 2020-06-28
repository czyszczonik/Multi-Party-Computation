class Protocol:
    def __init__(self, data):
        self.iniciator = data.get('iniciator', {})
        self.responder = data.get('responder', {})
        
