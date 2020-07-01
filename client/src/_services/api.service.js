import config from 'config';
import { authHeader } from '../_helpers'; 

export const apiService = {
    protocols,
    startProt,
    step1,
    step2,
    step3,
    step4
};

function protocols() {
    const requestOptions = {
        method: 'GET',
        headers: authHeader()
    };

    return fetch(`${config.apiUrl}/protocol`, requestOptions)
        .then(handleResponse)
        .then(protocols => {
                return protocols;
            }
        );
}

function startProt(name) {
    const requestOptions = {
        method: 'GET',
        headers: authHeader()
    };
    console.log(name);
    return fetch(`${config.apiUrl}/protocol/name/${name}`, requestOptions)
        .then(handleResponse)
        .then(protocol => {
                //TODO: test
                return protocol;
            }
        );
}

function step1(myName, theirName, encryptions, myChoice, cLabels, pubKey, otMessages) {
    const requestOptions = {
        method: 'POST',
        headers: { ...authHeader(), 'Content-Type': 'application/json' },
        body: JSON.stringify({
            iniciator: myName,
            responder: theirName,
            encryptions: encryptions,
            iniciatorChoice: myChoice,
            iniciatorLabels: cLabels,
            pubKey: pubKey,
            iniciatorMessages: otMessages
        })
    };

    return fetch(`${config.apiUrl}/protocol/step1`, requestOptions)
        .then(handleResponse)
        .then(msg => {
                //TODO: test
                return msg;
            }
        );
}


function step2(pId, responderName, v) {
    const requestOptions = {
        method: 'POST',
        headers: { ...authHeader(), 'Content-Type': 'application/json' },
        body: JSON.stringify({
            protocolId: pId,
            responder: responderName,
            v: v
        })
    };


    return fetch(`${config.apiUrl}/protocol/step2`, requestOptions)
        .then(handleResponse)
        .then(msg => {
                //TODO: test
                return msg;
            }
        );
}

function step3(pId, initiatorName, messages) {
    const requestOptions = {
        method: 'POST',
        headers: { ...authHeader(), 'Content-Type': 'application/json' },
        body: JSON.stringify({
            protocolId: pId,
            iniciator: initiatorName,
            messagesForResponder: messages
        })
    };

    console.log(requestOptions)
    return fetch(`${config.apiUrl}/protocol/step3`, requestOptions)
        .then(handleResponse)
        .then(msg => {
                //TODO: test
                return msg;
            }
        );
}

function step4(pId, responderName, responderLabel) {
    const requestOptions = {
        method: 'POST',
        headers: { ...authHeader(), 'Content-Type': 'application/json' },
        body: JSON.stringify({
            protocolId: pId,
            responder: responderName,
            responderLabels: responderLabel
        })
    };

    console.log(requestOptions)
    return fetch(`${config.apiUrl}/protocol/step4`, requestOptions)
        .then(handleResponse)
        .then(msg => {
                //TODO: test
                return msg;
            }
        );
}

function handleResponse(response) {
    return response.text().then(text => {
        const data = text && JSON.parse(text);
        return data;
    });
}
