<template>
    <div class="products">
        <ProductsItem v-for="product in suggestions" :key="product.ItemCode" v-bind="{product: product}"/>
    </div>
</template>

<script>
    import ProductsItem from "./ProductsItem"
    export default {
        components: {ProductsItem},
        props: ["suggestions"],
        data() {
            return {
                items: [1,2,3,4,5,6,7,8,9,10]
            }
        }
    };
</script>

<style scoped lang="scss">
    .products {
        direction: rtl;
        display: inline-grid;
        grid-template-columns: auto auto auto auto auto auto;
        grid-gap: 1em;
        /deep/.product {
            border: 1px solid black;
            .header {
                background: rgba(3, 3, 3, 0.12);
                border-bottom: 1px solid black;
                padding: 0.3em;
            }
            .body {
                display: flex;
                flex-direction: column;
                min-height: 150px;
                align-items: baseline;
                padding: 1em;
                padding-bottom: 0;
                .item {
                    display: block;
                }
                .image {
                    padding-top: 1em;
                }
            }
        }
    }
</style>