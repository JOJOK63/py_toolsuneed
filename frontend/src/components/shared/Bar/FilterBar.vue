<script setup lang="ts">
import ToggleBtn from '@/components/shared/Btn/ToggleBtn.vue'
import { ref } from 'vue'
import BaseInput from '@/components/shared/BaseInput.vue'

const isFilterActive = ref<boolean>(false)
const placeholder = ref<string>('test')
</script>

<template>
  <BaseInput :placeholder="placeholder"></BaseInput>
  <ToggleBtn label="" v-model:state="isFilterActive"></ToggleBtn>
</template>

<style scoped></style>
