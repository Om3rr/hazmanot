import VueRouter from 'vue-router'
import Vue from 'vue'
import AddProductsPage from '../components/AddProductsPage'
import Bar from '../components/Bar'

const routes = [
    { path: '/', component: AddProductsPage },
    { path: '/bar', component: Bar }
];
Vue.use(VueRouter);
export default new VueRouter({
    routes // short for `routes: routes`
})