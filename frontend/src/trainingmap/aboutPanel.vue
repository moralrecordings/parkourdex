<template>
    <div class="grid-container full">
        <center><img v-bind:src="logoUrl" title="parkourdex"/></center>
        <button class="close-button" type="button" v-on:click="$emit('showPanel', 'about', null)"><span aria-hidden="true">×</span></button>
    </div>
</template>
<style lang="scss">

</style>
<script>

import logoUrl from './assets/logo.svg';



export default {
    name: 'aboutPanel',
    data: function () {
        return {
            logoUrl: `${this.parkourdexUrl}${logoUrl}`
        };
    },
    props: {
        parkourdexUrl: String,
    },
    methods: {

    },
    mounted: function () {

    }
}

</script>
