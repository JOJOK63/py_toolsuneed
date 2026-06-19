<script setup lang="ts">
import { ref } from 'vue'
defineProps<{
  placeholder: string
}>()

const research = ref<string | null>(null)
</script>

<template>
  <input type="text" placeholder="{{placeholder}}" class="input" v-model="research" />
</template>

<style scoped></style>
