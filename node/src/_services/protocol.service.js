import config from 'config';
import { stringify } from 'querystring';

const crypto = require('crypto');
const CryptoJS = require('crypto-js');
var AES = CryptoJS.AES//require("crypto-js/aes");
var sha512 = CryptoJS.SHA512;
var sha256 = CryptoJS.SHA256;

export const protocolService = {
    initializeProtocol,
    // getCLabels,
    // obliviousTransferRound1,
    // startResponding,
    // obliviousTransferRound2,
    // obliviousTransferRound3,
    // obliviousTransferRound4,
    // findOutputLabels,
    // getResultLabels
};

//Potential try-catch
function _getProtocolData(protocolId) {
    return JSON.parse(localStorage.getItem('protocolInformation-'+protocolId)); 
}

function _setProtocolData(protocolId, obj) {
    localStorage.setItem('protocolInformation-'+protocolId, JSON.stringify(obj));
}

function _dec2hex (dec) {
    return ('0' + dec.toString(16)).substr(-2)
  }

function _getRandomString(length) {
    var arr = new Uint8Array((length) / 2)
    window.crypto.getRandomValues(arr)
    return Array.from(arr, dec2hex).join('')
  }

var JsonFormatter = {
    stringify: function(cipherParams) {
        // create json object with ciphertext
        var jsonObj = { ct: cipherParams.ciphertext.toString(CryptoJS.enc.Base64) };

        // optionally add iv or salt
        if (cipherParams.iv) {
            jsonObj.iv = cipherParams.iv.toString();
        }

        if (cipherParams.salt) {
            jsonObj.s = cipherParams.salt.toString();
        }

        // stringify json object
        return JSON.stringify(jsonObj);
    },
    parse: function(jsonStr) {
        // parse json string
        var jsonObj = JSON.parse(jsonStr);

        // extract ciphertext from json object, and create cipher params object
        var cipherParams = CryptoJS.lib.CipherParams.create({
            ciphertext: CryptoJS.enc.Base64.parse(jsonObj.ct)
        });

        // optionally extract iv or salt

        if (jsonObj.iv) {
            cipherParams.iv = CryptoJS.enc.Hex.parse(jsonObj.iv);
        }

        if (jsonObj.s) {
            cipherParams.salt = CryptoJS.enc.Hex.parse(jsonObj.s);
        }

        return cipherParams;
    }
};

//TODO: check, test
function _getGateLabels() {
    var a0 = _getRandomString(16)
    var a1 = _getRandomString(16)
    var b0 = _getRandomString(16)
    var b1 = _getRandomString(16)
    var c0 = _getRandomString(16)
    var c1 = _getRandomString(16)
    return {
        a0: a0,
        a1: a1,
        b0: b0,
        b1: b1,
        c0: c0,
        c1: c1
    }
}

function _shuffle(arrParam) {
    let arr = arrParam.slice(),
        length = arr.length,
        temp,
        i;

    while(length){
        i = Math.floor(Math.random() * length--);

        temp = arr[length];
        arr[length] = arr[i];
        arr[i] = temp;
    }

    return arr;
}

function _initEncryptionTable(labels){

    var k00 = labels['a0']+labels['b0'];
    var k01 = labels['a0']+labels['b1'];
    var k10 = labels['a1']+labels['b0'];
    var k11 = labels['a1']+labels['b1'];

    //TODO: check correctness
    var e00 = AES.encrypt(labels['c0'], k00, {
        format: JsonFormatter
    });
    var e01 = AES.encrypt(labels['c0'], k01, {
        format: JsonFormatter
    });
    var e10 = AES.encrypt(labels['c0'], k10, {
        format: JsonFormatter
    });
    var e11 = AES.encrypt(labels['c1'], k11, {
        format: JsonFormatter
    });

    var encryptions = [e00, e01, e10, e11];
    var shuffled = _shuffle(encryptions);

    return shuffled;
}

function initializeProtocol(protocolId, choice) {
    var data = {};
    data.labels = _getGateLabels();
    encryptionTable = _initEncryptionTable(protocolId);
    //TODO: maybe save a choice?
    choiceLabel = choice == 0 ? data.labels['c0'] : data.labels['c1'];
    
    _setProtocolData(bob, data);
    return [encryptionTable, choiceLabel];
}

function getCLabels(protocolId) {
    data = _getProtocolData(protocolId);
    var cLabels = {
        c0: data.labels['c0'],
        c1: data.labels['c1']
    };
    return cLabels;
}

function obliviousTransferRound1(protocolId) {
    data = _getProtocolData(protocolId);
    x0 = crypto.randomBytes(16);
    x1 = crypto.randomBytes(16);
    // https://github.com/travist/jsencrypt
    //TODO: implement
    // data.otRandoms = [x0, x1]
    // rsa = RSA.generate(1024) 
    // self.rsa[protocolId] = rsa
    // return (rsa.n, rsa.e),(x0, x1)
}

/////////////////////////////////////////////////////////////


function startResponding(protocolId, encryptions, mychoice, otherChoice) {
    var data = {};
    data.encryptions = encryptions;
    data.otherChoice = otherChoice;
    data.choice = mychoice;
    _setProtocolData(protocolId, data);
}


function obliviousTransferRound2(protocolId, pubKey, messages) {
    var data = _getProtocolData(protocolId);
    var n = pubKey[0];
    var e = pubKey[1];
    //TODO: implement
    // if data.choice in [0,1]:
    //     k = get_random_bytes(16)
    //     self.k[name] = k
    //     k = int(k.hex(), 16)
    //     xb = int(messages[self.choices[name]].hex(), 16)
    //     v = (xb+pow(k, e, n)) % n
    //     #TODO: convert v back to byte array (then convert to int in round3)
    //     return v
    // else:
    //     pass #TODO: handle unexpected situation
}

/////////////////////////////////////////////////////////////

function obliviousTransferRound3(protocolId, v) {
    //TODO: implement
    // privKey = self.rsa[name]
    // d = privKey.d
    // n = privKey.n
    // tempMessages = self.tempMessages[name]
    // x0 = int(tempMessages[0].hex(), 16)
    // x1 = int(tempMessages[1].hex(), 16)

    // k0 = pow(v-x0, d, n)
    // k1 = pow(v-x1, d, n)

    // b0 = int(self.labels[name]['b0'].hex(), 16)
    // b1 = int(self.labels[name]['b1'].hex(), 16)

    // m0 = b0 + k0
    // m1 = b1 + k1

    // m0 = m0.to_bytes(1024, 'big')
    // m1 = m1.to_bytes(1024, 'big') #TODO: can possibly be more, what then? Also bind to RSA keylength

    // return (m0, m1)
}

/////////////////////////////////////////////////////////////



function obliviousTransferRound4(protocolId, messages) {
    var data = _getProtocolData(protocolId);
    //TODO: implement
    // if self.choices[name] in [0,1]:
    // var k = int(self.k[name].hex(), 16)
    // var m = int(messages[self.choices[name]].hex(), 16)
    // var mb = m - k
    // var data.label = mb.to_bytes(16, 'big')
    // _setProtocolData(protocolId, data);
    //  else:
    //     pass #TODO: handle unexpected scenario
}


function findOutputLabels(protocolId) {
    var data = _getProtocolData(protocolId);
    var key = data.otherChoice+data.label;
    results = [];
    for (const encryption of data.encryptions) {
        dec = AES.decrypt(encryption, key).toString(CryptoJS.enc.Utf8);
        if (dec != "") {
            data.resultLabel = dec;
            return dec
        }
    }
    //TODO: assert we don't end up here
}
