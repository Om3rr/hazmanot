<template>
    <div>
        <input type="text" v-model="search" v-on:input="updateSuggestions()" v-on:keyup.enter="onEnter()">
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
            async onEnter() {
                await this.createProduct(this.search);
                this.search = null;
            },
            updateSuggestions: _.debounce(function(){this.suggest()}, 500),
            ...mapActions('products', ["addProduct", 'createProduct'])
        }
    }
</script>

<style scoped>

</style>