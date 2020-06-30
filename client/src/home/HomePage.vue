<template>
    <div>
        <h1>Hi {{account.user.firstName}}!</h1>
        {{users}}
        
        <div v-if="users.items[0]">
            <h3>{{users.items[0].firstName}} {{users.items[0].lastName}}, {{users.items[0].age}}</h3>
            <div id="picture">
                <!-- <img v-img :src="getImageUrl(users.items[0].firstName)" contain height="auto" width="100%" /> -->
            </div>
            <p>{{users.items[0].bio}}</p>
            <div id="buttons" class="row justify-content-around">
                <button class="btn btn-primary col-4" @click="dislike">&#10060;</button>
                <button class="btn btn-primary col-4" @click="like">&#128151;</button>
            </div>
        </div>
        <div v-else style="text-align: center;">
            <h2>You have swiped them all!</h2>
        </div>

        <div class="row justify-content-between" style="margin-top: 3em;">
            <div class="col-2">
                <router-link to="/login">Logout</router-link>
            </div>
            <div class="col-2">
                <router-link to="/profile">Profile</router-link>
            </div>
            <!-- <button class="btn btn-primary" @click="test">test</button> -->
        </div>
    </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
// import { protocolService } from '../_services';
// const CryptoJS = require('crypto-js');
// const crypto = require('crypto');
// var sha512 = require('crypto-js/sha512');
// var sha256 = require('crypto-js/sha256');
// var aes = require('crypto-js/aes');
// const rsa = require('node-rsa');


export default {
    computed: {
        ...mapState({
            account: state => state.account,
            users: state => state.users.all
        })
    },
    created () {
        this.getAllUsers();
        this.protocol();
    },
    methods: {
        ...mapActions('users', {
            deleteUser: 'delete',
            getAllUsers: 'getAll'
        }),
        ...mapActions('protocol', {
            getProtocols: 'getProtocols'
        }),
        like () {
            console.log('Like');
            this.users.items.shift();
        },
        dislike () {
            console.log('Dislike');
        },
        test () {
            var k = sha256('2123');
            var c0 = aes.encrypt("Message", "Secret Passphrase");
            var c1 = aes.encrypt("Message", "Secret Passphrase");
            console.log('-----------------');
            // protocolService.__testProtocol();
        },
        protocol() {
            var p;
            while (true) {
                setTimeout(() => {
                        p = this.getProtocols;
                        console.log(p);
                }, 2000)
            }
        },
        getImageUrl(name) {
            return "https://thispersondoesnotexist.com/image?"+name;
        }
    }
};
</script>