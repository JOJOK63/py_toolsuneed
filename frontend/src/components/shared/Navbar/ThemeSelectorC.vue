<script setup lang="ts">
import themes from 'daisyui/theme/object'
import { PaintRoller } from 'lucide-vue-next'

const themeList = Object.keys(themes)
</script>

<template>
  <div class="dropdown">
    <div tabindex="0" role="button" class="btn">
      <PaintRoller />
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
