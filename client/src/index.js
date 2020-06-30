import Vue from 'vue';
import VeeValidate from 'vee-validate';
import VueImg from 'v-img';

import { store } from './_store';
import { router } from './_helpers';
import App from './app/App';

Vue.use(VeeValidate);
Vue.use(VueImg);

// import { configureFakeBackend } from './_helpers/fake-backend';
// configureFakeBackend();

new Vue({
    el: '#app',
    router,
    store,
    render: h => h(App)
});