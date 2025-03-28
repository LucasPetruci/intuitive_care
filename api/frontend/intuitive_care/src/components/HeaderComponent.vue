<template>
  <header class="main-header">
    <img src="../assets/intuitive-care.png" alt="Logo" class="logo" />
  </header>
</template>

<script>
export default {
  name: "HeaderComponent",
};
</script>

<style scoped>
.main-header {
  display: flex;
  align-items: flex-start;
  padding: 1rem;
  background-color: white; 
  border-bottom: 1px solid #ccc
}

.logo {
  padding-left: 4rem;
  height: 50px; 
  margin-right: 1rem;
}

</style>
