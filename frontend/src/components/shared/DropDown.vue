<script setup lang="ts">
defineProps({
  label: String,
})

const dropdownChoices = defineModel<string[]>('dropdownChoices', { default: () => [] })
const dropdownSelection = defineModel('dropdownSelection', { default: '' })

const selectedItem = (item: string) => {
  dropdownSelection.value = item
}
</script>

<template>
  <div class="dropdown">
    <div tabindex="0" role="button" class="btn m-1">
      {{ dropdownSelection || 'Filtrer' }}
    </div>
    <ul tabindex="-1" class="dropdown-content menu bg-base-100 rounded-box z-1 w-52 p-2 shadow-sm">
      <li v-for="item in dropdownChoices" :key="item">
        <a @click="selectedItem(item)">{{ item }}</a>
      </li>
    </ul>
  </div>
</template>

<style scoped></style>
