import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import * as mutationTypes from './mutation_types';

Vue.use(Vuex);

const API_HOST = `${process.env.VUE_APP_API_PROTOCOL}://${process.env.VUE_APP_API_HOSTNAME}`;

export default new Vuex.Store({
  state: {
    me: null,
  },
  mutations: {
    [mutationTypes.UPDATE_ME](state, data) {
      state.me = data;
    },
  },
  actions: {
    async get_me({ commit }) {
      return axios.get(`${API_HOST}/api/me`)
        .then(({ data }) => commit(mutationTypes.UPDATE_ME, data))
        .catch(() => commit(mutationTypes.UPDATE_ME, null));
    },
  },
});
