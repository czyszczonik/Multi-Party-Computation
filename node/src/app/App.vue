<template>
    <div class="container" style="margin-top: 1em;">
        <div class="row">
            <div class="col-sm-6 offset-sm-3">
                <div class="jumbotron">
                    <router-view></router-view>
                    <div v-if="alert.message" :class="`alert ${alert.type}`">{{alert.message}}</div>
                </div>
            </div>
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