<script setup lang="ts">
defineProps<{
  placeholder: string
}>()

const research = defineModel<string>('research')
</script>

<template>
  <input type="text" :placeholder="placeholder" class="input" v-model="research" />
</template>

<style scoped></style>
