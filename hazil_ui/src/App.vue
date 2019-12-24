<template>
  <div id="app">
    <MainBar v-if="loggedIn"/>
    <!-- route outlet -->
    <!-- component matched by the route will render here -->
    <router-view></router-view>
  </div>
</template>

<script>
import {mapActions, mapState} from 'vuex'
import MainBar from "./components/MainBar";
export default {
  name: 'app',
  components: {MainBar},
  mounted() {
      this.initUser();
    },
    methods: {
        ...mapActions('user', {initUser: "initUser"})
    },
    computed: {
      ...mapState('user', {loggedIn: "loggedIn"})
    }

}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
