<template>
    <div>
        <!-- <h1>Hi {{account.user.firstName}}!</h1>
        <br><br>
        <div v-if="users.items">
            <h3>{{users.items[0].firstName}} {{users.items[0].lastName}}, {{users.items[0].age}}</h3>
            <div id="picture">
                <img v-img v-if="users.items[0].imageUrl" :src="users.items[0].imageUrl" contain height="auto" width="100%" />
            </div>
            <p>{{users.items[0].bio}}</p>
            <div id="buttons">
                <button class="btn btn-primary" @click="dislike">&#10060;</button>
                <button class="btn btn-primary" @click="like">&#128151;</button>
            </div>
        </div> -->




        <!-- <em v-if="users.loading">Loading users...</em> -->
        <!-- <span v-if="users.error" class="text-danger">ERROR: {{users.error}}</span> -->
        <!-- <ul v-if="users.items">
            <li v-for="user in users.items" :key="user.id">
                {{user.firstName + ' ' + user.lastName}}
                <span v-if="user.deleting"><em> - Deleting...</em></span>
                <span v-else-if="user.deleteError" class="text-danger"> - ERROR: {{user.deleteError}}</span>
                <span v-else> - <a @click="deleteUser(user.id)" class="text-danger">Delete</a></span>
            </li>
        </ul> -->
        <p>
            <router-link to="/login">Logout</router-link>
        </p>
        <p>
            <router-link to="/profile">Profile</router-link>
        </p>
        <button class="btn btn-primary" @click="test">test</button>
    </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import { protocolService } from '../_services';


const CryptoJS = require('crypto-js');
const crypto = require('crypto');
var sha512 = require('crypto-js/sha512');
var sha256 = require('crypto-js/sha256');
var aes = require('crypto-js/aes');
const rsa = require('node-rsa');


export default {
    computed: {
        ...mapState({
            account: state => state.account,
            users: state => state.users.all
        })
    },
    created () {
        this.getAllUsers();
    },
    methods: {
        ...mapActions('users', {
            deleteUser: 'delete',
            getAllUsers: 'getAll'
        }),
        like () {
            console.log('Like')
            this.users.items.shift()
        },
        dislike () {
            console.log('Dislike')
        },
        test () {
            var k = sha256('2123')
            var c0 = aes.encrypt("Message", "Secret Passphrase");
            var c1 = aes.encrypt("Message", "Secret Passphrase");
            // console.log(k);
            // console.log(c0);
            // console.log(c1);
            // console.log(crypto);
            // console.log(CryptoJS);
            // console.log(rsa);
            console.log('-----------------');
            protocolService.__testProtocol();
        }
    }
};
</script>