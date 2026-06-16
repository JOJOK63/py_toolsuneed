<script setup lang="ts">
import { useRoute } from 'vue-router'

const route = useRoute()

const props = defineProps<{
  onClose: () => void
}>()
</script>

<template>
  <li>
    <RouterLink
      to="/todolist"
      @click="props.onClose"
      :class="{ active: route.path === '/todolist' }"
    >
      Todo Board
    </RouterLink>
  </li>
</template>

<style scoped></style>
