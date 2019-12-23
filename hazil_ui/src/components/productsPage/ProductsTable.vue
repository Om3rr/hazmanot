<template>
    <div class="products">
        <div class="products--line products--header">
            <div class="products--line--item--small products--header">תיאור</div>
            <div class="products--line--item products--header">מחיר</div>
            <div class="products--line--item products--header">מק"ט</div>
            <div class="products--line--item products--header">כמות</div>
            <div class="products--line--item products--header">הוסף</div>
        </div>
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
        display: flex;
        flex-direction: column;
        /deep/ &--line {
            padding: 0.3em 0.5em;
            &.products--header {
                padding: 1em 0.5em;
                border-bottom: 1px solid #ccc;
                font-weight: 500;
                color: #fff;
                background: linear-gradient(to bottom, rgba(234,47,44,1) 0%,rgba(174,41,10,1) 100%);
            }
            flex: auto;
            display: flex;
            flex-direction: row;
            &--item {
                flex: 1 1 0;
                text-align: right;
                &--small {
                    flex: 1 1 0;
                    text-align: right;
                }
                input {
                    width: 15%;
                    text-align: center;
                }
            }
        }
    }
</style>