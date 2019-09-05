import Vue from 'vue';
import Router from 'vue-router';
import store from './store';
import Home from './views/Home.vue';
import Main from './views/Main.vue';

Vue.use(Router);

function isAuth() {
  return store.state.me != null;
}

const requireAuth = () => (from, to, next) => {
  if (isAuth()) return next();
  return next('/');
};

const requireUnAuth = () => (from, to, next) => {
  if (!isAuth()) return next();
  return next('/main');
};

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
      beforeEnter: requireUnAuth(),
    },
    {
      path: '/main',
      name: 'main',
      component: Main,
      beforeEnter: requireAuth(),
    },
    // {
    //   path: '/about',
    //   name: 'about',
    //   component: () => import(/* webpackChunkName: "about" */ './views/About.vue'),
    // },
  ],
});
