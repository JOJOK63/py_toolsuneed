<script setup lang="ts">
import ChildTest from '@/views/ChildTest.vue'
import { ref } from 'vue'

const name = ref<string>('jhon')

function danger() {
  alert('test')
}
</script>

<template>
  <h1>mon test</h1>
  <ChildTest>
    <template #aaaa>
      <h1>This is the header</h1>
    </template>

    <template #default>
      <p>This is the content</p>
    </template>

    <template #footer>
      <em>This is the footer</em>
    </template>
  </ChildTest>

  <input type="text" v-model="name" />
  <button @click.prevent="danger()">ok</button>
  <p>{{ name }}</p>
</template>

<style scoped></style>
