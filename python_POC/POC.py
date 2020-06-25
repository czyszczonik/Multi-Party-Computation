from Party import Party
from Server import Server
import time


def presentProtocol(aliceChoice, bobChoice):
    alice = Party('alice')
    bob = Party('bob')
    server = Server()


    # Protocol round 1
    encryptions, ac = alice.InitializeProtocol(bob.name, aliceChoice)
    aliceLabels = alice.getCLabels(bob.name)
    pubKey, aliceMessages = alice.obliviousTransferRound1(bob.name)
    server.putRound1(encryptions, ac, aliceLabels, pubKey, aliceMessages)


    # Protocol round 2
    encryptions, ac, pubKey, aliceMessages = server.getRound2()
    bob.startResponding(alice.name, encryptions, bobChoice, ac)
    v = bob.obliviousTransferRound2(alice.name, pubKey, aliceMessages)
    server.putRound2(v)


    # Protocol round 3
    v = server.getRound3()
    bobMessages = alice.obliviousTransferRound3(bob.name, v)
    server.putRound3(bobMessages)


    # Protocol round 4
    bobMessages = server.getRound4()
    bob.obliviousTransferRound4(alice.name, bobMessages)
    bob.findOutputLabels(alice.name)
    bobLabels = bob.getResultLabels(alice.name)
    server.putRound4(bobLabels)

    return server.computeResult()


def performTests(iterations):
    print("_" * 50)
    print(f"Running {4 * iterations} iterations of protocol")
    ts = time.time()
    for _ in range(iterations):
        for firstChoice in [0,1]:
            for secondChoice in [0,1]:
                assert presentProtocol(firstChoice, secondChoice) == (firstChoice and secondChoice), f'ERROR for inputs {firstChoice}, {secondChoice}'
    te = time.time()
    print(f'Time elapsed: {te-ts}s.\nTime per one exchange: {(te-ts)/(4*iterations)}')
    print("_" * 50)

if __name__ == "__main__":
    iterations = 10
    performTests(iterations)
#TODO list: Possibly improve the overall flow



def obliviousTransferRound1(self, name):
    try:
        self.choices[name]
    except:
        print(f'{self.name} has not made a choice about {name} \nOT cannot happen')
        exit(1)
    x0 = get_random_bytes(16)
    x1 = get_random_bytes(16)
    self.tempMessages[name] = (x0, x1)
    rsa = RSA.generate(1024)
    self.rsa[name] = rsa
    return (rsa.n, rsa.e),(x0, x1)
