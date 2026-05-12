<script setup lang="ts">
import { PlusIcon } from '@heroicons/vue/24/outline'

const emit = defineEmits<{
  click: []
}>()
</script>

<template>
  <button class="btn btn-ghost btn-outline btn-sm" @click="emit('click')">
    <PlusIcon class="w-4 h-4" />
  </button>
</template>
