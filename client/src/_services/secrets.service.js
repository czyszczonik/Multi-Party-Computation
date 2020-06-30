import config from 'config';
import {stringify} from "querystring";
import { authHeader } from '../_helpers'; 
const CryptoJS = require('crypto-js');
var AES = CryptoJS.AES;

export const secretsService = {
  createSecret,
  getSecrets
};

function createSecret(username, protocolId){
  var data = AES.encrypt(plaintext, key, {
      format: JsonFormatter
  });
}

function getSecrets(protocolId) {
    var secrets = localStorage.getItem('protocolInformation-'+protocolId);
    
    //TODO: test
    if (secrets) {
        return secrets;
    }
    
    const requestOptions = {
        method: 'GET',
        headers: authHeader()
    };
    return fetch(`${config.apiUrl}/secret/${protocolId}`, requestOptions)
        .then(handleResponse)
        .then(
            secret => {
                    var pass = localStorage.getItem('secretPassword');
                    var data = decrypt(secret.data, pass)
                    localStorage.setItem('protocolInformation-'+protocolId, data);
                    return data;
            }
        );
}

function sendSecret(username, protocolId) {
    var key = localStorage.getItem('secretPassword');
    var secretData = localStorage.getItem('protocolInformation-'+protocolId);
    var data = encrypt(secretData, key);

    const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, protocolId, data })
    };
    return fetch(`${config.apiUrl}/secret`, requestOptions);
}

function decrypt(encryption, key) {
  return AES.decrypt(encryption, key).toString(CryptoJS.enc.Utf8);
}



function encrypt(encryption, key) {
  return AES.encrypt(encryption, key, {
      format: JsonFormatter
  });
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
        console.log(jsonObj);
        return JSON.stringify(jsonObj);
    }
};

function handleResponse(response) {
    return response.text().then(text => {
        const data = text && JSON.parse(text);
        return data;
    });
}
