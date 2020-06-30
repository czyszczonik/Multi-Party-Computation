import config from 'config';
import { authHeader } from '../_helpers'; 
import { stringify } from 'querystring';

const crypto = require('crypto');
var sha512 = require('crypto-js/sha512');
var sha256 = require('crypto-js/sha256');

export const userService = {
    login,
    logout,
    register,
    getAll,
    update,
    delete: _delete,
    getData,
    getSalt,
    swipe
};

function login(username, pass, salt) {
    var password = sha512(pass+salt);
    var secretPassword = sha256(salt+pass);
    const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
    };

    return fetch(`${config.apiUrl}/auth/login`, requestOptions)
        .then(handleResponse)
        .then(
            user => {
                if (user.username) {
                    localStorage.setItem('user', JSON.stringify(user));
                    localStorage.setItem('secretPassword', secretPassword);
                }
            }
        );
}

//TODO: check
function logout() {
    const requestOptions = {
        method: 'GET',
    };
    return fetch(`${config.apiUrl}/auth/logout`);
}

function register(user) {
    user.salt = crypto.randomBytes(128).toString('base64')
    user.password = sha512(user.password+user.salt)

    const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(user)
    };

    return fetch(`${config.apiUrl}/auth/register`, requestOptions).then(handleResponse);

}

function getAll() {
    const requestOptions = {
        method: 'GET',
        headers: authHeader()
    };

    return fetch(`${config.apiUrl}/users`, requestOptions).then(handleResponse);
}

function update(userData) {
    const requestOptions = {
        method: 'PUT',
        headers: {'Content-Type': 'application/json' },
        body: JSON.stringify(userData)
    };

    return fetch(`${config.apiUrl}/profile`, requestOptions).then(handleResponse);
}

//TODO: implement
function swipe(user, choice) {
    const requestOptions = {
        method: 'POST',
    };
    return
}

// delete is a reserved word in javascript
//TODO: modify
function _delete(id) {
    const requestOptions = {
        method: 'DELETE',
        headers: authHeader()
    };

    return fetch(`${config.apiUrl}/users/${id}`, requestOptions).then(handleResponse);
}

function getData() {
    const requestOptions = {
        method: 'GET'
    };
    return fetch(`${config.apiUrl}/profile`)

}

function getSalt(username) {
    const requestOptions = {
        method: 'GET'
    };

    return fetch(`${config.apiUrl}/auth/salt/${username}`, requestOptions).then(handleResponse);
}

function handleResponse(response) {
    return response.text().then(text => {
        const data = text && JSON.parse(text);
        if (!response.ok) {
            if (response.status === 401) {
                // auto logout if 401 response returned from api
                logout();
                location.reload(true);
            }

            const error = (data && data.message) || response.statusText;
            return Promise.reject(error);
        }

        return data;
    });
}