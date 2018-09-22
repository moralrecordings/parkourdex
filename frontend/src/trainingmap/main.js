import '../ieHacks.js';

import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);
Vue.config.productionTip = (process.env.NODE_ENV === 'production');

//import store from './store.js';
import main from './main.vue';


var trainingMapApp = function (target, parkourdexUrl, mapboxToken) {
    var options = {
        props: {parkourdexUrl, mapboxToken}
    };

    /* eslint-disable no-new */
    return new Vue({
        //store,
        render: function (h) {
            return h(main, options);
        }
    }).$mount(target);
};


export default trainingMapApp
