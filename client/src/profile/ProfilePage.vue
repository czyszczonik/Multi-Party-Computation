<template>
    <div class="col-sm-6 offset-sm-3">
        <div class="jumbotron">
            <div>
                <h1>{{account.user.firstName}} {{account.user.lastName}}</h1>
                <h2>Your profile</h2>
                <form @submit.prevent="handleSubmit">
                    <div class="form-group">
                        <label for="phone">Phone number</label>
                        <input type="text" v-model="account.user.phone" name="phone" class="form-control"/>
                    </div>
                    <!-- <div class="form-group">
                        <label for="preview">Profile picture</label>
                        <input type="file" accept="image/jpeg" @change=uploadImage>
                        <div id="preview">
                            <img v-img v-if="this.img" :src="`data:image/png;base64,${this.img}`" contain height="auto" width="100%" />
                            <img v-img v-else :src="`data:image/png;base64,${account.user.imageUrl}`" contain height="auto" width="100%" />
                        </div>
                    </div> -->
                    <div class="form-group">
                        <label for="age">Age</label>
                        <input type="number" v-model="account.user.age" name="age" class="form-control"/>
                    </div>
                    <div class="form-group">
                        <label for="bio">Bio</label>
                        <textarea v-model="account.user.bio" name="bio" class="form-control"/>
                    </div>
                    <div class="form-group">
                        <button class="btn btn-primary" style="margin-right: 1em;">Save</button>
                        <router-link to="/" style="margin-right: 1em;" >back</router-link>
                        <!-- <span v-if="user.deleting"><em> - Deleting...</em></span>
                        <span v-else-if="user.deleteError" class="text-danger"> - ERROR: {{user.deleteError}}</span> <span v-else-->
                        
                        <span><a @click="deleteUser(account.user.username)" class="text-danger">Delete account</a></span>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
    data () {
        return {
            img: '',
        }
    },
    computed: {
        ...mapState({
            account: state => state.account,
        })
    },
    created () {

    },
    methods: {
        ...mapActions('users', {
            getUserData: 'getData',
            deleteUser: 'delete',
            update: 'update'
        }),
        handleSubmit (e) {
            this.submitted = true;
            const userData = this.account.user;
            this.update(userData);
        },
        uploadImage (e) {
                const file = e.target.files[0];
                const reader = new FileReader();
                reader.onload = (e) => {
                    var image = e.target.result;
                    this.img = image;
                };
                reader.readAsDataURL(file);
        },
    }
};
</script>