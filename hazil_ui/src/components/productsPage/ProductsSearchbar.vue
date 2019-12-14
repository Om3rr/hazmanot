<template>
    <div>
        <input v-model="search" v-on:input="onInput" type="text"/>
    </div>
</template>

<script>
    import _ from "lodash";

    export default {
        data() {
            return {
                search: "",
                products: []
            }
        },
        methods: {
            emitInput() {
                this.$emit('input', this.search)
            },
            onInput: _.debounce(function(){this.emitInput()}, 500),
        }
    };
</script>

<style scoped>

</style>