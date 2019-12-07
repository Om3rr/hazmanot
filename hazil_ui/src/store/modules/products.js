import Vue from 'vue'
const state = {
    products: {}
}

const getters = {
    totalPrice(state) {
        return Object.values(state.products).map(p => p.ItemPrice * p.amount).reduce((a,b) => a+b, 0)
    }
}

const actions = {
    addProduct({commit}, product) {
        commit('PRODUCT_ADD', product)
    },
    deleteProduct({commit}, product) {
        commit("PRODUCT_DELETE", product)
    }
}

const mutations = {
    PRODUCT_ADD(state, product) {
        if(product.ItemCode in state.products) {
            const old_product = state.products[product.ItemCode];
            Vue.set(state.products, product.ItemCode, {...old_product, amount: (old_product.amount + 1)})
        } else {
            Vue.set(state.products, product.ItemCode, {...product, amount: 1})
        }
    },
    PRODUCT_DELETE(state, product) {
        if(state.products[product.ItemCode].amount == 1) {
            Vue.delete(state.products, product.ItemCode)
        } else {
            Vue.set(state.products[product.ItemCode], 'amount', state.products[product.ItemCode].amount - 1)
        }
    }
}

export default {
    state,
    getters,
    mutations,
    actions,
    namespaced: true,
}