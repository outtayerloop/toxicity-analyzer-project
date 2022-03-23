<template>
  <Home/>
  <Footer/>
</template>

<script>
import Home from './components/Home.vue'
import Footer from './components/Footer.vue'

export default {
  name: 'App',
  components: {
    Home,
    Footer
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
