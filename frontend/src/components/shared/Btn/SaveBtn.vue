<script setup lang="ts">
const emit = defineEmits<{ click: [] }>()
</script>

<template>
  <button class="btn btn-success btn-sm" @click="emit('click')">Sauvegarder</button>
</template>
