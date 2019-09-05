<template>
  <div class="twitch-sign-in">
    <m-button
      raised
      class="button"
      :href="api_base + '/logout'"
    >
      <font-awesome-icon slot="icon" :icon="iconTwitch" />
      Twitch 로그아웃
    </m-button>
  </div>
</template>

<script>
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { faTwitch } from '@fortawesome/free-brands-svg-icons';
import Button from 'material-components-vue/dist/button';
import Vue from 'vue';

Vue.use(Button);

export default {
  name: 'TwitchSignOutButton',
  data() {
    return {
      iconTwitch: faTwitch,
    };
  },
  computed: {
    api_base() {
      return `${process.env.VUE_APP_API_PROTOCOL}://${process.env.VUE_APP_API_HOSTNAME}`;
    },
  },
  components: {
    FontAwesomeIcon,
  },
};
</script>

<style scoped lang="scss">
  @import "../global.scss";
  @import "~material-components-vue/dist/button/styles";
  .button {
    @include mdc-button-filled-accessible(shade(#6441A4, 20));
    width: 200px;
  }
</style>
