<template>
    <div>
        <h1>{{account.user.firstName}} {{account.user.lastName}}</h1>
        <h2>Your profile</h2>
        <form @submit.prevent="handleSubmit">
            <div class="form-group">
                <label for="phone">Phone number</label>
                <input type="text" v-model="phone" name="phone" class="form-control"/>
            </div>
            <div class="form-group">
                <label for="preview">Profile picture</label>
                <input type="file" accept="image/jpeg" @change=uploadImage>
                <div id="preview">
                    <img v-img v-if="imageUrl" :src="imageUrl" contain height="auto" width="100%" />
                </div>
            </div>
            <div class="form-group">
                <label for="age">Age</label>
                <input type="number" v-model="age" name="age" class="form-control"/>
            </div>
            <div class="form-group">
                <label for="bio">Bio</label>
                <textarea v-model="bio" name="bio" class="form-control"/>
            </div>
            <div class="form-group">
                <button class="btn btn-primary" style="margin-right: 1em;">Save</button>
                <router-link to="/" style="margin-right: 1em;" >back</router-link>
                <!-- <span v-if="user.deleting"><em> - Deleting...</em></span>
                <span v-else-if="user.deleteError" class="text-danger"> - ERROR: {{user.deleteError}}</span> <span v-else-->
                
                <span><a @click="deleteUser(account.user.id)" class="text-danger">Delete account</a></span>
            </div>
        </form>

    </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
    data () {
        return {
            age: '',
            bio: '',
            submitted: false,
            imageUrl: '',
            phone: ''
        }
    },
    computed: {
        ...mapState({
            account: state => state.account,
        })
    },
    created () {
        userData = this.getUserData();
        this.age = userData['age'] || '';
        this.bio = userData['bio'] || '';
        this.imageUrl = userData['imageUrl'] || '';
        this.phone = userData['phone'] || '';
    },
    methods: {
        ...mapActions('users', {
            getUserData: 'getData',
            deleteUser: 'delete',
            update: 'update'
        }),
        handleSubmit (e) {
            this.submitted = true;
            var userData = {
                age: this.age,
                bio: this.bio,
                imageUrl: this.imageUrl,
                phone: this.phone
            };
            this.update(userData);
        },
        uploadImage (e) {
                const file = e.target.files[0]
                this.image = file
                this.imageUrl = URL.createObjectURL(file)
        },
    }
};
</script>