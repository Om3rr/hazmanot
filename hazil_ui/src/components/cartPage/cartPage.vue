<template>
    <div>
        {{ products }}
    </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
    computed: {
        ...mapState('products', ['products']),
    },
}
</script>

<style scoped></style>
