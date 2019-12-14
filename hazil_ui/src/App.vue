<template>
  <div id="app">
    <h1>Hello {{username}}</h1>
    <!-- route outlet -->
    <!-- component matched by the route will render here -->
    <router-view></router-view>
  </div>
</template>

<script>
import {mapActions, mapState} from 'vuex'
export default {
  name: 'app',
    mounted() {
      this.initUser();
    },
    methods: {
        ...mapActions('user', {initUser: "initUser"})
    },
    computed: {
        ...mapState('user', {username: 'username'})
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
  margin-top: 60px;
}
</style>
