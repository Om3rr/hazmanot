import {getMe} from "../../apis/orders";

const state = {
    username: null,
    email: null,
    profile_pic: null,
    orders: 0,
}

const getters = {

}

const mutations = {
    LOGIN(state, {username, email, profile_pic, orders}) {
        state.username = username
        state.email = email
        state.profile_pic = profile_pic
        state.orders = orders
    }
}

const actions = {
    async initUser({commit}) {
        commit('LOGIN', await getMe())
    }
}


export default {
    namespaced: true,
    state,
    actions,
    mutations,
    getters
}