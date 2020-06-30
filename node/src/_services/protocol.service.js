import config from 'config';
import { stringify } from 'querystring';
import { enc } from 'crypto-js';
import { PassThrough } from 'stream';

const crypto = require('crypto');
const CryptoJS = require('crypto-js');
const AES = CryptoJS.AES;
const RSA = require('node-rsa');


export const protocolService = {
    initializeProtocol,
    getCLabels,
    obliviousTransferRound1,
    startResponding,
    obliviousTransferRound2,
    obliviousTransferRound3,
    obliviousTransferRound4,
    findOutputLabels,
    getResultLabel,
    __testProtocol
};

//Potential try-catch
function _getProtocolData(protocolId) {
    return JSON.parse(localStorage.getItem('protocolInformation-'+protocolId)); 
}

function _setProtocolData(protocolId, obj) {
    // console.log(obj);
    localStorage.setItem('protocolInformation-'+protocolId, JSON.stringify(obj));
}

function _dec2hex (dec) {
    return ('0' + dec.toString(16)).substr(-2)
  }

function _getRandomString(length) {
    var arr = new Uint8Array((length) / 2)
    window.crypto.getRandomValues(arr)
    return Array.from(arr, _dec2hex).join('')
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

    var e00 = AES.encrypt(labels['c0'], k00).toString();
    var e01 = AES.encrypt(labels['c0'], k01).toString();
    var e10 = AES.encrypt(labels['c0'], k10).toString();
    var e11 = AES.encrypt(labels['c1'], k11).toString();  

    var encryptions = [e00, e01, e10, e11];
    var shuffled = _shuffle(encryptions);
    return shuffled;
}

function initializeProtocol(protocolId, choice) {
    var data = {};
    data.labels = _getGateLabels();
    var encryptionTable = _initEncryptionTable(data.labels);
    //TODO: maybe save a choice?
    var choiceLabel = choice == 0 ? data.labels['a0'] : data.labels['a1'];
    
    _setProtocolData(protocolId, data);
    return [encryptionTable, choiceLabel];
}

function getCLabels(protocolId) {
    var data = _getProtocolData(protocolId);
    var cLabels = {
        c0: data.labels['c0'],
        c1: data.labels['c1']
    };
    return cLabels;
}

function bnToBuf(bn) {
    var hex = BigInt(bn).toString(16);
    if (hex.length % 2) { hex = '0' + hex; }
  
    var len = hex.length / 2;
    var u8 = new Uint8Array(len);
  
    var i = 0;
    var j = 0;
    while (i < len) {
      u8[i] = parseInt(hex.slice(j, j+2), 16);
      i += 1;
      j += 2;
    }
  
    return u8;
}

function bufToBn(buf) {
    var hex = [];
    var u8 = Uint8Array.from(buf);
  
    u8.forEach(function (i) {
      var h = i.toString(16);
      if (h.length % 2) { h = '0' + h; }
      hex.push(h);
    });
  
    return BigInt('0x' + hex.join(''));
}

var modexp = function(a, b, mod) {
    a = a % mod;
    var result = BigInt(1);
    var x = a;
  
    while(b > 0){
      var leastSignificantBit = b % BigInt(2);
      b = b / BigInt(2);
  
      if (leastSignificantBit == 1) {
        result = result * x;
        result = result % mod;
      }
  
      x = x * x;
      x = x % mod;
    }
    return result;
  };

function obliviousTransferRound1(protocolId) {
    var data = _getProtocolData(protocolId);
    var x0 = bufToBn(crypto.randomBytes(16)).toString(16);
    var x1 = bufToBn(crypto.randomBytes(16)).toString(16);
    data.otRandoms = [x0, x1];
    var rsa = new RSA();
    rsa.generateKeyPair(); 
    var n = BigInt(rsa.keyPair.n.toString()).toString(16);
    var d = BigInt(rsa.keyPair.d.toString()).toString(16);
    var e = BigInt(rsa.keyPair.e).toString(16);
    data.rsa = {
        n: n.toString(16),
        d: d.toString(16),
        e: e.toString(16)
    };

    _setProtocolData(protocolId, data);
    return [[n, e], [x0, x1]];
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
    var n = BigInt('0x'+pubKey[0]);
    var e = BigInt('0x'+pubKey[1]);
    if (data.choice == 0 || data.choice == 1) {
        var k = bufToBn(crypto.randomBytes(16));
        data.k = k.toString(16);
        var xb = BigInt('0x'+messages[data.choice]);
        var val = modexp(k, e, n);
        var v = xb+val
        _setProtocolData(protocolId, data);
        return v.toString(16)
    }
    else {
        console.log(`Critical error, OT round 2. Protocol ID ${protocolId}, data:`);
        console.log(data);
    }
        
}

/////////////////////////////////////////////////////////////

function obliviousTransferRound3(protocolId, v) {
    var data = _getProtocolData(protocolId);
    var rsaKey = data.rsa;
    var d = BigInt('0x'+rsaKey.d);
    var n = BigInt('0x'+rsaKey.n);
    var tempMessages = data.otRandoms;

    var x0 = BigInt('0x'+tempMessages[0]);
    var x1 = BigInt('0x'+tempMessages[1]);
    var v = BigInt('0x'+v);

    var dd = v-x1;

    var k0 = modexp(v-x0, d, n)
    var k1 = modexp(v-x1, d, n)

    var b0 = BigInt('0x'+data.labels['b0']);
    var b1 = BigInt('0x'+data.labels['b1']);

    var m0 = b0 + k0
    var m1 = b1 + k1

    return [m0.toString(16), m1.toString(16)]
}

/////////////////////////////////////////////////////////////

function obliviousTransferRound4(protocolId, messages) {
    var data = _getProtocolData(protocolId);
    if (data.choice == 0 || data.choice == 1) {
        var k = BigInt('0x'+data.k);
        var m = BigInt('0x'+messages[data.choice]);
        var mb = m - k;
        data.label = mb.toString(16)
        _setProtocolData(protocolId, data);
    }
}


function findOutputLabels(protocolId) {
    var data = _getProtocolData(protocolId);
    var key = data.otherChoice+data.label;
    var dec;
    var encryptions = data.encryptions;
    // console.log(encryptions);
    // console.log(key);
    encryptions.forEach(function (elem) {
        dec = CryptoJS.AES.decrypt(elem, key);
        // console.log(dec);
        try {
            dec = dec.toString(CryptoJS.enc.Utf8);
            if (dec != "") {
                console.log('succ');
                data.resultLabel = dec;
            }
        }
        //TODO: deciphering sometimes throws errors - check if it's the labels' fault or something https://stackoverflow.com/questions/58111929/why-i-get-malformed-utf-8-data-error-on-crypto-js
        catch (e){console.log('err')}
            // console.log(dec);
    });
    _setProtocolData(protocolId, data);
    return data.resultLabel;
}

function getResultLabel(protocolId) {
    var data = _getProtocolData(protocolId);
    return data.resultLabel;
}

function __testProtocol(){
    var aliceChoice = 1;
    var bobChoice = 1;
    var encryptions;
    var ac;
    var pubKey;
    var OTMessages;

    [encryptions, ac] = initializeProtocol('bob', aliceChoice)
    var cLabels = getCLabels('bob');
    [pubKey, OTMessages] = obliviousTransferRound1('bob');
    // server.putRound1(encryptions, ac, cLabels, pubKey, aliceMessages)

    // encryptions, ac, pubKey, aliceMessages = server.getRound2()
    startResponding('alice', encryptions, bobChoice, ac)
    var v = obliviousTransferRound2('alice', pubKey, OTMessages)
    // server.putRound2(v)


    // v = server.getRound3()
    var bobMessages = obliviousTransferRound3('bob', v)
    // server.putRound3(bobMessages)

    // bobMessages = server.getRound4()
    obliviousTransferRound4('alice', bobMessages)
    var outputL = findOutputLabels('alice')
    // server.putRound4(bobLabels)

    console.log(cLabels);
    console.log(outputL);
}
