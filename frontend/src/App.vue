<template>
  <v-app>
    <Header />
    <v-content>
      <router-view />
    </v-content>
  </v-app>
</template>

<script>
import Header from "./components/Header"
export default {
  name: "App",
  components: {
    Header
  }
}
</script>

<style>
#app {
  background-color: #eeeeee;
}
</style>
