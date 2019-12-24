<template>
    <div class="products-page">
        <ProductsSearchbar class="searchbar" v-on:input="suggest" :search="search"/>
        <ProductsTable class="products-table" :suggestions="suggestions"/>
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
            } else {
                await this.suggest()
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

<style scoped lang="scss">
    .products-page {
        display: flex;
        flex-direction: column;
        max-height: inherit;
        .products-table {
            overflow-y: auto;
            max-height: 100%;
        }
    }
</style>