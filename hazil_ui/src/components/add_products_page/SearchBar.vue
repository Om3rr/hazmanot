<template>
    <div>
        <input type="text" v-model="search" v-on:input="updateSuggestions()">
        <div v-for="product in products" :key="product.ItemCode" @click="addProduct(product)">
            {{product.ItemName}} - {{product.ItemPrice}}
        </div>
    </div>
</template>

<script>
    import {suggestProducts} from "../../apis/products";
    import {mapActions} from 'vuex'
    import _ from 'lodash'
    export default {
        name: "SearchBar",
        data() {
            return {
                search: "",
                products: []
            }
        },
        methods: {
            async suggest() {
               this.products = await suggestProducts(this.search)
            },
            updateSuggestions: _.debounce(function(){this.suggest()}, 500),
            ...mapActions('products', ["addProduct"])
        }
    }
</script>

<style scoped>

</style>