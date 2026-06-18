<script setup lang="ts">
import { onMounted, ref, watch, watchEffect } from 'vue'

const monInput = ref()
const timer = ref(0)
const show = ref(false)
let interval: ReturnType<typeof setInterval> | undefined = undefined

onMounted(() => {
  monInput.value.focus()

  interval = setInterval(() => {
    timer.value += 1
  }, 1000)
})

watch(show, (newValue) => {
  if (newValue === true) {
    clearInterval(interval)
    interval = undefined
  } else {
    interval = setInterval(() => {
      timer.value += 1
    }, 1000)
  }
})

watchEffect(() => {
  console.log(show.value)
})
</script>

<template>
  <h1>Test enfant</h1>
  <input type="text" ref="monInput" autofocus />
  <button class="btn" @click="show = !show">change</button>
  <p>TIMER : {{ timer }}</p>
  <div v-if="show">MON MINUTEUR</div>
</template>

<style scoped></style>
