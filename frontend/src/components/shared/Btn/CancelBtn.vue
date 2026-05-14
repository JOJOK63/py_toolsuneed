<script setup lang="ts">
const emit = defineEmits<{ click: [] }>()
</script>

<template>
  <button class="btn btn-ghost btn-sm" @click="emit('click')">Annuler</button>
</template>
