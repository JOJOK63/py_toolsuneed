<script setup lang="ts">
import ChildTest from '@/views/ChildTest.vue'
import CancelBtn from '@/components/shared/Btn/CancelBtn.vue'

function coucou() {
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
</template>

<style scoped></style>
