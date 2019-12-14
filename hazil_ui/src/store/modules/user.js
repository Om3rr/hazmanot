import {getMe} from "../../apis/orders";

const state = {
    username: null,
    email: null,
    profilePic: null,
    orders: 0,
    loggedIn: false,
    loading: true
}

const getters = {

}

const mutations = {
    LOGIN(state, {username, email, profile_pic, orders}) {
        state.loggedIn = true
        state.loading = false
        state.username = username
        state.email = email
        state.profilePic = profile_pic
        state.orders = orders
    },
    LOGIN_FAILED(state) {
        state.loggedIn = false;
        state.loading = false
    }
}

const actions = {
    async initUser({commit}) {
        try{
            const user = await getMe()
            commit('LOGIN', user)
        }
        catch (err) {
            commit("LOGIN_FAILED")
        }
    }
}


export default {
    namespaced: true,
    state,
    actions,
    mutations,
    getters
}