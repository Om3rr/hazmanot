<template>
    <div class="products-container">
        <div class="products">
        <ProductsItem v-for="product in suggestions" :key="product.ItemCode" v-bind="{product: product}"/>
    </div>
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
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        /deep/.product {
            flex: 0 1 11em;
            border: 1px solid black;
            margin: 1em;
            border-radius: 1em;
            display: flex;
            flex-direction: column;
            .header {
                background: rgba(3, 3, 3, 0.12);
                border-bottom: 1px solid black;
                padding: 0.3em;
                border-top-left-radius: 1em;
                border-top-right-radius: 1em;
            }
            .body {
                display: flex;
                flex-direction: column;
                min-height: 150px;
                align-items: baseline;
                flex: auto;
                div {
                    width: 100%;
                }
                .item {
                    display: block;
                    padding: .3em .8em;
                }
                .image {
                    padding-top: 1em;
                    img { object-fit: cover; height: 7em;}
                    flex: auto;
                }
                .price {
                    background: #cccccc;
                    border-top: 1px solid black;
                    border-bottom-left-radius: 1em;
                    border-bottom-right-radius: 1em;
                }
            }
        }
    }
</style>