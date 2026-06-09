<script setup lang="ts">
import { ref, watch } from 'vue'
import type { SubcategoryCreate } from '@/api/modules/budget/category.ts'
import CreateBtn from '@/components/shared/Btn/CreateBtn.vue'

const emit = defineEmits<{
  submit: [data: SubcategoryCreate]
}>()
</script>

<template>
  <h1 class="uppercase">crud form</h1>
</template>

<style scoped></style>
