<template>
  <div class="main">
    <TwitchSignOutButton />
  </div>
</template>

<script>

import TwitchSignOutButton from '../components/TwitchSignOutButton.vue';

export default {
  name: 'main',
  components: { TwitchSignOutButton },
};
</script>

<style scoped lang="scss">
  @import "../global.scss";
</style>
