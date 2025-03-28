<template>
  <div id="app">
    <HeaderComponent />
    <SearchComponent />
    <FooterComponent />
  </div>
</template>

<script>
import HeaderComponent from "./components/HeaderComponent.vue";
import SearchComponent from "./components/SearchComponent.vue";
import FooterComponent from "./components/FooterComponent.vue";

export default {
  name: "App",
  components: {
    HeaderComponent,
    SearchComponent,
    FooterComponent
  },
};
</script>

<style>

</style>
