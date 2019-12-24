import VueRouter from 'vue-router'
import Vue from 'vue'
import ProductsPage from '../components/productsPage/ProductsPage'
import LoginPage from '../components/loginPage/LoginPage'
import ProductPage from '../components/productPage/ProductPage'
import AuthPage from '../components/AuthPage'
import store from '../store'

const meta = {requiresAuth: true};
const routes = [
    {path: '/', component: ProductsPage, meta},
    {path: '/products/:productId', component: ProductPage, meta},
    {path: '/user/login', component: LoginPage, meta: {requiresAuth: false}},
    {path: '/user/auth', component: AuthPage},
];
Vue.use(VueRouter);
const router = new VueRouter({
    mode: 'history',
    routes // short for `routes: routes`
});

router.beforeEach((to, from, next) => {
    if (to.matched.some(route => route.meta.requiresAuth)) {
        if (store.state.user.loggedIn) {
            next();
        } else {
            next({path: '/user/auth', query: {redirect: to.path, query: to.query}});
        }
    }
    next();
});

export default router;