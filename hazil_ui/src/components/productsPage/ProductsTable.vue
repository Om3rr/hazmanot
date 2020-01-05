<template>
    <div class="products-container">
        <div class="products">
            <component
                :key="product.ItemCode"
                v-bind="{ product: product }"
                v-bind:is="productItemComponent"
                v-for="product in suggestions"
            ></component>
        </div>
    </div>
</template>

<script>
import ProductsItem from './ProductsItem'
import ProductsItemMobile from './ProductsItemMobile'

export default {
    components: { ProductsItem, ProductsItemMobile },
    props: ['suggestions'],
    computed: {
        productItemComponent() {
            return this.isMobile ? ProductsItemMobile : ProductsItem
        },
        isMobile() {
            return true
        },
    },
}
</script>

<style lang="scss" scoped>
.products {
    direction: rtl;
    display: flex;
    justify-content: right;
    flex-wrap: wrap;

    /deep/ .product--mobile {
        display: flex;
        width: 100%;
        justify-content: space-evenly;
        flex-direction: row;
        font-size: 0.8em;
        .item {
            flex: 1 0 0;
            &--nogrow {
                flex: 0 0 0;
                img {
                    object-fit: cover;
                    height: 2em;
                }
            }
        }
    }
    /deep/ .product {
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
                padding: 0.3em 0.8em;
            }

            .image {
                padding-top: 1em;

                img {
                    object-fit: cover;
                    height: 7em;
                }

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
