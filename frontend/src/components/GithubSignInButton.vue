<template>
  <div class="twitch-sign-in">
    <m-button
      raised>
      <font-awesome-icon slot="icon" :icon="iconGithub" />
      Github 로그인
    </m-button>
  </div>
</template>

<script>
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { faGithub } from '@fortawesome/free-brands-svg-icons';
import Button from 'material-components-vue/dist/button';
import Vue from 'vue';

Vue.use(Button);

export default {
  name: 'GithubSignInButton',
  data() {
    return {
      iconGithub: faGithub,
    };
  },
  components: {
    FontAwesomeIcon,
  },
};
</script>

<style scoped lang="scss">
  @import "../global.scss";
  @import "~material-components-vue/dist/button/styles";
  .twitch-sign-in button {
    @include mdc-button-filled-accessible(#333333)
  }
</style>
