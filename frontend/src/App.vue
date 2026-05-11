<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import AppNavbar from '@/components/shared/Navbar/AppNavbar.vue'
</script>

<template>
  <header>
    <AppNavbar></AppNavbar>
  </header>
  <RouterView />
</template>

<style scoped>
@media (min-width: 1024px) {

}
</style>
