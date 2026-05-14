<!-- ButtonSubmit.vue -->
<script setup lang="ts">
const props = defineProps<{
  label?: string
}>()
</script>

<template>
  <button class="btn btn-primary mt-2" type="submit">
    {{ props.label ?? 'Créer' }}
  </button>
</template>
