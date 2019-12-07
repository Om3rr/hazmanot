<template>
    <div>
        <SearchBar/>
        ------------
        <CurrentCart/>
    </div>
</template>

<script>
    import SearchBar from "./add_products_page/SearchBar";
    import CurrentCart from "./add_products_page/CurrentCart";
    export default {
        name: "AddProductsPage",
        components: {CurrentCart, SearchBar}
    }
</script>

<style scoped>

</style>