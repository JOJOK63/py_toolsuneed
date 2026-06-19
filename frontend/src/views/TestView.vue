<script setup lang="ts">
import ChildTest from '@/views/ChildTest.vue'
import ToggleBtn from '@/components/shared/Btn/ToggleBtn.vue'
import { ref } from 'vue'
import FilterBar from '@/components/shared/Bar/FilterBar.vue'

const isFilterActive = ref(false)
</script>

<template>
  <h1>TEST Parent</h1>
  <FilterBar :isFilterActive="isFilterActive"></FilterBar>
  <ToggleBtn label="test" v-model:state="isFilterActive"></ToggleBtn>
  <p v-if="!isFilterActive">show</p>
  <ChildTest></ChildTest>
</template>
<style scoped></style>
