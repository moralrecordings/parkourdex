<template>
    <div class="grid-container full">
        <h3>parkourdex</h3>
        <button class="close-button" type="button" v-on:click="$emit('showPanel', 'about', null)"><span aria-hidden="true">×</span></button>
    </div>
</template>
<style lang="scss">

</style>
<script>

export default {
    name: 'aboutPanel',
    data: function () {
        return {

        };
    },
    props: {
        
    },
    methods: {

    },
    mounted: function () {

    }
}

</script>
