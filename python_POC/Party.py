from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes, random
import secrets, string
get_random_string = lambda size: ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(size)).encode()

class Party():


    def __init__(self, name):
        #Assume that name is globally unique
        self.name = name

        #Required for the initiator
        self.keys = {}
        self.results = {}
        self.tempMessages = {}
        self.rsa = {}

        #Required for the responder
        self.encryptions = {}
        self.otherChoices = {}
        self.k = {}
        self.resultLabels = {} #Potentially not necessary, requires some thinking

        #Required for both
        self.labels = {}
        self.choices = {}



    ########################################################
    # ROUND 1                                              #
    ########################################################


    def InitializeProtocol(self, name, choice):
        self.labels[name] = self._getGateLabels(name)
        encryptionTable = self._initEncryptionTable(name)
        choiceLabel = self._getSetChoiceLabel(name, choice)
        return encryptionTable, choiceLabel


    def getCLabels(self, name):
        labels = {
            'c0': self.labels[name]['c0'],
            'c1': self.labels[name]['c1']
        }
        return labels


    def obliviousTransferRound1(self, name):
        try:
            self.choices[name]
        except:
            print(f'{self.name} has not made a choice about {name}\nOT cannot happen')
            exit(1) #TODO: change
        x0 = get_random_bytes(16)
        x1 = get_random_bytes(16)
        self.tempMessages[name] = (x0, x1)
        rsa = RSA.generate(1024) #TODO: Benchmark and change
        self.rsa[name] = rsa
        return (rsa.n, rsa.e),(x0, x1)


    def _getGateLabels(self, name):
        a0 = get_random_string(16)
        a1 = get_random_string(16)
        b0 = get_random_string(16)
        b1 = get_random_string(16)
        c0 = get_random_string(16)
        c1 = get_random_string(16)
        return {
            'a0': a0,
            'a1': a1,
            'b0': b0,
            'b1': b1,
            'c0': c0,
            'c1': c1
        }


    def _initEncryptionTable(self, name):
        labels = self.labels[name]

        k00 = labels['a0']+labels['b0']
        c00 = AES.new(k00, AES.MODE_EAX)

        k01 = labels['a0']+labels['b1']
        c01 = AES.new(k01, AES.MODE_EAX)

        k10 = labels['a1']+labels['b0']
        c10 = AES.new(k10, AES.MODE_EAX)

        k11 = labels['a1']+labels['b1']
        c11 = AES.new(k11, AES.MODE_EAX)

        self.keys[name] = [k00, k01, k10, k11]

        #This block would differ for other logic gates/circuits
        e00 = (c00.encrypt(labels['c0']), c00.nonce)
        e01 = (c01.encrypt(labels['c0']), c01.nonce)
        e10 = (c10.encrypt(labels['c0']), c10.nonce)
        e11 = (c11.encrypt(labels['c1']), c11.nonce)

        encryptions = [e00, e01, e10, e11]
        random.shuffle(encryptions)

        return encryptions


    def _getSetChoiceLabel(self, name, choice):
        if choice == 0:
            self.choices[name] = self.labels[name]['a0']
        else:
            self.choices[name] = self.labels[name]['a1']
        return self.choices[name]


    ########################################################
    # ROUND 2                                              #
    ########################################################


    def startResponding(self, name, encryptions, mychoice, otherChoice):
        self.encryptions[name] = encryptions
        self.otherChoices[name] = otherChoice
        self.choices[name] = mychoice


    def obliviousTransferRound2(self, name, pubKey, messages):
        try:
            self.choices[name]
        except:
            print(f'{self.name} has not made a choice about {name}\nOT cannot happen')
            exit(2) #TODO: change
        n = pubKey[0] #TODO: potentially remember public key for the Initiator?
        e = pubKey[1]
        if self.choices[name] in [0,1]:
            k = get_random_bytes(16)
            self.k[name] = k
            k = int(k.hex(), 16)
            xb = int(messages[self.choices[name]].hex(), 16)
            v = (xb+pow(k, e, n)) % n
            #TODO: convert v back to byte array (then convert to int in round3)
            return v
        else:
            pass #TODO: handle unexpected situation


    ########################################################
    # ROUND 3                                              #
    ########################################################


    def obliviousTransferRound3(self, name, v):
        #TODO: assert that x0 x1 are set, just like the RSA key
        privKey = self.rsa[name]
        d = privKey.d
        n = privKey.n
        tempMessages = self.tempMessages[name]
        x0 = int(tempMessages[0].hex(), 16)
        x1 = int(tempMessages[1].hex(), 16)

        k0 = pow(v-x0, d, n)
        k1 = pow(v-x1, d, n)

        b0 = int(self.labels[name]['b0'].hex(), 16)
        b1 = int(self.labels[name]['b1'].hex(), 16)

        m0 = b0 + k0
        m1 = b1 + k1

        m0 = m0.to_bytes(1024, 'big')
        m1 = m1.to_bytes(1024, 'big') #TODO: can possibly be more, what then? Also bind to RSA keylength

        return (m0, m1)


    ########################################################
    # ROUND 4                                              #
    ########################################################


    def obliviousTransferRound4(self, name, messages):
        #TODO: assert the responder's choice is known by the responder
        if self.choices[name] in [0,1]:
            #TODO: assert the responder doesn't have anything in labels[name]
            k = int(self.k[name].hex(), 16)
            m = int(messages[self.choices[name]].hex(), 16)
            mb = m - k
            self.labels[name] = mb.to_bytes(16, 'big')
        else:
            pass #TODO: handle unexpected scenario


    def findOutputLabels(self, name):
        #TODO: assert self.labels[name] is known
        #TODO: assert self.resultLabels[name] is empty

        #NOTE: normally responder recieves only one label, but the implementation prevents
        #"Bob" from rejecting incorrect "labels", this one is something that needs to be addressed #TODO!!!!
        key = self.otherChoices[name]+self.labels[name]
        results = []
        for (enc, nonce) in self.encryptions[name]:
            try:
                cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
                dec = cipher.decrypt(enc)
                dec.decode()
                results += [dec]
            except:
                pass
        self.resultLabels[name] = results
        assert len(results) == 1


    def getResultLabels(self, name):
        return self.resultLabels[name]
