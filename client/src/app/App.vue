<template>
    <div class="container" style="margin-top: 1em;">
        <div class="row">
            <router-view></router-view>
            <div v-if="alert.message" :class="`alert ${alert.type}`">{{alert.message}}</div>
        </div>
    </div>

</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
    name: 'app',
    computed: {
        ...mapState({
            alert: state => state.alert
        })
    },
    methods: {
        ...mapActions({
            clearAlert: 'alert/clear' 
        })
    },
    watch: {
        $route (to, from){
            // clear alert on location change
            this.clearAlert();
        }
    } 
};
</script>