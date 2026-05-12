<script setup lang="ts">
import { TrashIcon } from '@heroicons/vue/24/outline'

const emit = defineEmits<{
  click: []
}>()
</script>

<template>
  <button class="btn btn-error btn-outline btn-sm" @click="emit('click')">
    <TrashIcon class="w-4 h-4" />
  </button>
</template>

<style scoped></style>
