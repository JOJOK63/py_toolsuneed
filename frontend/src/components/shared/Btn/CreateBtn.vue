<!-- ButtonSubmit.vue -->
<script setup lang="ts">
const props = withDefaults(defineProps<{ label?: string }>(), {
  label: 'Créer',
})
</script>

<template>
  <button class="btn btn-primary mt-2" type="submit">
    {{ props.label ?? 'Créer' }}
  </button>
</template>
