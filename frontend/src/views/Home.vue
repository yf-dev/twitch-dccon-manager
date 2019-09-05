<template>
  <div class="home">
    <div class="top-layout">
      <div class="dccons-wrapper">
        <div class="dccons">
          <div class="dccon dccon-1">
            <img src="../assets/march.png" alt="(대충 마치 콘)">
          </div>
          <div class="dccon dccon-2">
            <img src="../assets/power.png" alt="(대충 힘의차이 콘)">
          </div>
          <div class="dccon dccon-3">
            <img src="../assets/vaultboy.png" alt="(대충 볼트공중 콘)">
          </div>
        </div>
      </div>
      <div class="title-wrapper">
        <h1 class="title">
          TWITCH DCCON MANAGER
        </h1>
      </div>
    </div>
    <div class="sign-in-button">
      <TwitchSignInButton class="sign-in"/>
    </div>
  </div>
</template>

<script>

import TwitchSignInButton from '../components/TwitchSignInButton.vue';

export default {
  name: 'home',
  components: { TwitchSignInButton },
};
</script>

<style scoped lang="scss">
  @import "../global.scss";

  .top-layout {
    max-width: 1000px;
    margin: 0 auto;
  }

  .dccons {
    margin: 60px auto;
    width: 250px;
    position: relative;
  }

  .dccon {
    height: 100px;
    width: 100px;
    overflow: hidden;
    position: absolute;
    background: #ffffff;
    border: solid 1px shade($tdm-gray, 50);

    img {
      height: 100px;
      width: 100px;
    }
  }

  .dccon-1 {
    top: 30px;
    left: 0;
    transform: rotate(-15deg);
  }

  .dccon-2 {
    top: 0;
    left: 70px;
    transform: rotate(0deg);
  }

  .dccon-3 {
    top: 30px;
    left: 140px;
    transform: rotate(15deg);
  }

  .title-wrapper {
    position: relative;
    padding-top: 170px;
  }

  .title {
    margin: 0 auto;
    display: block;
    position: relative;
    text-align: center;
  }

  .sign-in-button {
    width: 200px;
    margin: 0 auto;
    padding-top: 24px;
  }

  .sign-in {
    display: inline-block;
  }
</style>
