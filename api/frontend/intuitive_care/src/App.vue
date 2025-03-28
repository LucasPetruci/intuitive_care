<template>
  <div id="app">
    <HeaderComponent />
    <SearchComponent />
  </div>
</template>

<script>
import HeaderComponent from "./components/HeaderComponent.vue";
import SearchComponent from "./components/SearchComponent.vue";

export default {
  name: "App",
  components: {
    HeaderComponent,
    SearchComponent,
  },
};
</script>

<style>

</style>
