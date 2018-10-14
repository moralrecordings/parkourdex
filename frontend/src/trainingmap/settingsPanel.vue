<template>
    <div class="grid-container full">
        <h3>Settings</h3>
        <div class="grid-x">
            Signed in as {{ user.username }}. 
        </div>
        <div class="grid-x">
            <button class="button expanded" v-on:click="signOut">Sign out</button>
        </div>
        <button class="close-button" type="button" v-on:click="$emit('showPanel', 'settings', null)"><span aria-hidden="true">×</span></button>        
    </div>
</template>
<style lang="scss">

</style>
<script>

import { submitLogout } from './api.js';


export default {
    name: 'settingsPanel',
    data: function () {
        return {
        };
    },
    props: {
        parkourdexUrl: String,
        user: Object,
    },
    methods: {
        signOut: function () {
            var vm = this;
            submitLogout(vm.parkourdexUrl, function (data) {
                vm.$emit('login', data);
            }, function (error) {
                console.log(error);
            });
        }
    },
    mounted: function () {

    },
}

</script>
