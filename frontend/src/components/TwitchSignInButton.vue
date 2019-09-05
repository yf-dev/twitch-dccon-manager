<template>
  <div class="twitch-sign-in">
    <m-button
      raised
      class="button"
      :href="api_base + '/login'"
    >
      <font-awesome-icon slot="icon" :icon="iconTwitch" />
      Twitch 로그인
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
  name: 'TwitchSignInButton',
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
    @include mdc-button-filled-accessible(#6441A4);
    width: 200px;
  }
</style>
