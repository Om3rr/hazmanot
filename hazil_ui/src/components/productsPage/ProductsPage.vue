<template>
    <div>
        <ProductsSearchbar v-on:input="suggest" :search="search"/>
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
                suggestions: [],
                search: ''
            }
        },
        async mounted() {
            if(this.$route.query.query) {
                await this.suggest(this.$route.query.query);
            }
        },
        methods: {
            async suggest(query) {
                this.search = query;
                this.suggestions = await suggestProducts(query)
                this.$router.push({ query: { query }})
            },
        }
    };
</script>

<style scoped>

</style>