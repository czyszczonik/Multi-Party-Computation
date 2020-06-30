import config from 'config';
import { authHeader } from '../_helpers'; 

export const apiService = {
    protocols,
    step1
};

function protocols() {
    const requestOptions = {
        method: 'GET',
        headers: authHeader()
    };

    return fetch(`${config.apiUrl}/protocol`, requestOptions)
        .then(handleResponse)
        .then(protocols => {
                //TODO: test
                return protocols;
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

// function protocols() {
//     const requestOptions = {
//         method: 'GET',
//         headers: authHeader()
//     };

//     return fetch(`${config.apiUrl}/protocol`, requestOptions)
//         .then(handleResponse)
//         .then(protocols => {
//                 //TODO: test
//                 return protocols;
//             }
//         );
// },

// function protocols() {
//     const requestOptions = {
//         method: 'GET',
//         headers: authHeader()
//     };

//     return fetch(`${config.apiUrl}/protocol`, requestOptions)
//         .then(handleResponse)
//         .then(protocols => {
//                 //TODO: test
//                 return protocols;
//             }
//         );
// },
