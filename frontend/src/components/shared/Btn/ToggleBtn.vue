<script setup lang="ts">
defineProps({
  label: String,
})

const state = defineModel<boolean>('state', { default: false })
</script>

<template>
  <div class="flex gap-2 p-2">
    <p>{{ label }}</p>
    <label class="toggle text-base-content">
      <input type="checkbox" v-model="state" />
      <svg aria-label="enabled" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
        <g
          stroke-linejoin="round"
          stroke-linecap="round"
          stroke-width="4"
          fill="none"
          stroke="currentColor"
        >
          <path d="M20 6 9 17l-5-5"></path>
        </g>
      </svg>
      <svg
        aria-label="disabled"
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        stroke-width="4"
        stroke-linecap="round"
        stroke-linejoin="round"
      >
        <path d="M18 6 6 18" />
        <path d="m6 6 12 12" />
      </svg>
    </label>
  </div>
</template>

<style scoped></style>
