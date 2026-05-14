<script setup lang="ts">
import { PencilIcon } from '@heroicons/vue/24/outline'
const emit = defineEmits<{ click: [] }>()
</script>

<template>
  <button class="btn btn-primary btn-outline btn-sm" @click="emit('click')">
    <PencilIcon class="w-4 h-4" />
  </button>
</template>
