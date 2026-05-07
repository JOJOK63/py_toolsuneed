<script setup lang="ts">
import themes from 'daisyui/theme/object'

const themeList = Object.keys(themes)
</script>

<template>
  <div class="dropdown">
    <div tabindex="0" role="button" class="btn">
      Theme
      <svg
        width="12px"
        height="12px"
        class="inline-block h-2 w-2 fill-current opacity-60"
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 2048 2048"
      >
        <path d="M1799 349l242 241-1017 1017L7 590l242-241 775 775 775-775z"></path>
      </svg>
    </div>
    <ul tabindex="-1" class="dropdown-content bg-base-300 rounded-box z-1 w-52 p-2 shadow-2xl">
      <li v-for="theme in themeList" :key="theme">
        <label class="block cursor-pointer px-4 py-2 hover:bg-base-200 rounded-lg">
          <input
            type="radio"
            name="theme-dropdown"
            class="theme-controller hidden"
            :value="theme"
          />
          <span class="capitalize">
            {{ theme }}
          </span>
        </label>
      </li>
    </ul>
  </div>
</template>

<style scoped></style>
