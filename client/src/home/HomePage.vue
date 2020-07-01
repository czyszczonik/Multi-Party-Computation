<template>
    <div class="row" style="width: 100%;">
        <div class="col-sm-6 offset-sm-3">
            <div class="jumbotron">
                <div>
                    <h1>Hi {{account.user.firstName}}!</h1>
                    <div v-if="users.all.items[0]">
                        <h3>{{users.all.items[0].firstName}} {{users.all.items[0].lastName}}, {{users.all.items[0].age}}</h3>
                        <div id="picture">
                            <img v-img :src="getImageUrl(users.all.items[0])" contain height="auto" width="100%" />
                        </div>
                        <p>{{users.all.items[0].bio}}</p>
                        <div id="buttons" class="row justify-content-around">
                            <button class="btn btn-primary col-4" @click="dislike">&#10060;</button>
                            <button class="btn btn-primary col-4" @click="like">&#128151;</button>
                        </div>
                    </div>
                    <div v-else style="text-align: center;">
                        <h2>You have swiped them all!</h2>
                        <h3>Wait for more users to join</h3>
                    </div>

                    <div class="row justify-content-between" style="margin-top: 3em;">
                        <div class="col-2">
                            <router-link to="/login">Logout</router-link>
                        </div>
                        <div class="col-2">
                            <router-link to="/profile">Profile</router-link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-sm-3">
            <div class="jumbotron">
                <div>
                    <h2>Your matches</h2>
                    <div v-if="users.all.matches.length">
                        <ol>
                            <div v-for="match in users.all.matches">
                                <li>
                                    <div style="border 1px, margin:auto">
                                {{match.firstName}} {{match.lastName}}, {{match.age}} <br>
                                Phone number: {{match.phone}}
                                    </div>
                                </li>
                            </div>
                        </ol>
                    </div>
                    <div v-else style="text-align: center;">
                        <h4>When you match with someone, they will appear here</h4>
                    </div>
                </div>
            </div>
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
            users: state => state.users,
        })
    },
    created () {
        this.getAllUsers();
        this.protocol();
        this.matches();
    },
    methods: {
        ...mapActions('users', {
            deleteUser: 'delete',
            getAllUsers: 'getAll',
            getMatches: 'getMatches'
        }),
        ...mapActions('protocol', {
            getProtocols: 'getProtocols',
            startProt: 'startProt'
        }),
        like () {
            console.log('Like');
            var user = this.users.all.items.shift();
            var name = user.username;
            var choice = 1;
            console.log(name);
            this.startProt({ choice, name });
        },
        dislike () {
            var user = this.users.all.items.shift();
            var name = user.username;
            var choice = 0;
            this.startProt({ choice, name });
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
            setInterval(() => {
                p = this.getProtocols();
                // console.log(p);
            }, 3000)
        },
        matches() {
            setInterval(() => {
                this.getMatches();
            }, 3000)
        },
        getImageUrl(user) {
            var uname = user.username;
            // return "https://thispersondoesnotexist.com/image?"+uname;
            return "https://thiscatdoesnotexist.com/?"+uname;
        }
    }
};
</script>