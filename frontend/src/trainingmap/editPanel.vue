<template>
    <div class="grid-container full">
        <h3>Add new spot</h3>
        <div class="grid-x">
            <label class="formControl">Name
                <input type="text"/>
            </label>
        </div>
        <div class="grid-x">
            <label class="formControl">Description
                <textarea />
            </label>
        </div>
        <div class="grid-x expanded button-group">
            <button class="button">Save</button>
            <button class="button secondary" v-on:click="$emit('toggleMode', 'default')">Cancel</button>
        </div>
        <button class="close-button" type="button" v-on:click="$emit('toggleMode', 'default')"><span aria-hidden="true">×</span></button>
    </div>
</template>
<style lang="scss">
label.formControl {
    width: 100%;
}

label.formControl textarea {
    height: 8em;
}
</style>
<script>

export default {
    name: 'detailPanel',
    data: function () {
        return {

        };
    },
    props: {
        parkourdexUrl: String 
    },
    methods: {

    },
    mounted: function () {

    }
}

</script>
