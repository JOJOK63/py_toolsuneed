<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import AppNavbar from '@/components/shared/Navbar/AppNavbar.vue'
import { ref } from 'vue'

const research = ref('')
</script>

<template>
  <header>
    <AppNavbar v-model:search="research"></AppNavbar>
  </header>
  <RouterView />
</template>

<style scoped>
@media (min-width: 1024px) {
}
</style>
