<template>
    <div class="grid-container full">
        <div class="text-center" style="margin-bottom: 1em;">
            <img v-bind:src="logoUrl" title="parkourdex"/>
        </div>
        <div class="grid-x" v-if="errorMessage">
            <div class="callout alert">
                {{ errorMessage }}
            </div>
        </div>
        <form v-on:submit.prevent="signin">
            <div class="grid-x">
                <input type="text" name="username" placeholder="Username" v-model="username"/>
            </div>
            <div class="grid-x">
                <input type="password" name="password" placeholder="Password" v-model="password"/>
            </div>
            <div class="grid-x">
                <input type="submit" class="button expanded" value="Sign in" />
            </div>
        </form>
        <div class="text-center">
            <a target="_blank" v-bind:href="`${parkourdexUrl}/password_reset/`" >Forgot your password?</a>
            <hr style="width: 100%"/>
        </div>
        <div class="grid-x">
            <a target="_blank" v-bind:href="`${parkourdexUrl}/register/`" class="button expanded success">Register</a>
        </div>

        <p class="text-center">
            <small>
                Made by <a href="https://twitter.com/moralrecordings">@moralrecordings</a> for <a href="https://perthparkour.com">Perth Parkour</a><br/> 
                <a href="https://bitbucket.org/moralrecordings/parkourdex">Source code</a> - <a href="#">Terms of service</a> - <a href="mailto:abuse@parkourdex.org">Report abuse</a><br/>
            </small>
        </p>
        <button class="close-button" type="button" v-on:click="$emit('showPanel', 'login', null)"><span aria-hidden="true">×</span></button>
    </div>
</template>
<style lang="scss">

</style>
<script>

import logoUrl from './assets/logo.svg';

import { submitLogin } from './api.js';


export default {
    name: 'loginPanel',
    data: function () {
        return {
            username: '',
            password: '',
            logoUrl: `${this.parkourdexUrl}${logoUrl}`,
            errorMessage: null,
        };
    },
    props: {
        parkourdexUrl: String,
        login: Object,
    },
    methods: {
        signin: function () {
            var vm = this;
            this.errorMessage = null;
            submitLogin(vm.parkourdexUrl, JSON.stringify({
                username: vm.username,
                password: vm.password
            }), function (data) {
                vm.$emit('login', data);
            }, function (error) {
                vm.errorMessage = error;
            });
        }
    },
    mounted: function () {

    }
}

</script>
