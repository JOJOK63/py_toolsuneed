<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import AppNavbar from '@/components/shared/Navbar/AppNavbar.vue'
</script>

<template>
  <header>

    <div class="wrapper">
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
      </nav>
    </div>
    <AppNavbar></AppNavbar>
  </header>

  <RouterView />
</template>




<style scoped>

@media (min-width: 1024px) {

}
</style>
