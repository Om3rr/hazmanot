import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import GAuth from 'vue-google-oauth2'
const gauthOption = {
  clientId: '1058655073238-ekt0nlii7eb17p8r0jkqtj4is1rspo4i.apps.googleusercontent.com',
  scope: 'profile',
  prompt: 'select_account'
}
Vue.use(GAuth, gauthOption)
Vue.config.productionTip = false

new Vue({
    render: h => h(App),
    store,
    router
}).$mount('#app')
