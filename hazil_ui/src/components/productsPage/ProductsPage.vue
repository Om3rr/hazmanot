<template>
    <div>
        <ProductsSearchbar v-on:input="suggest"/>
        <ProductsTable :suggestions="suggestions"/>
    </div>
</template>

<script>
    import ProductsTable from './ProductsTable'
    import ProductsSearchbar from "./ProductsSearchbar";
    import {suggestProducts} from "../../apis/products";
    export default {
        components: {ProductsSearchbar, ProductsTable},
        data() {
            return {
                suggestions: []
            }
        },
        methods: {
            async suggest(query) {
               this.suggestions = await suggestProducts(query)
            },
        }
    };
</script>

<style scoped>

</style>