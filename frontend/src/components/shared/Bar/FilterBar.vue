<script setup lang="ts">
import ToggleBtn from '@/components/shared/Btn/ToggleBtn.vue'
import BaseInput from '@/components/shared/BaseInput.vue'
import DropDown from '@/components/shared/DropDown.vue'
import DeleteBtn from '@/components/shared/Btn/DeleteBtn.vue'

withDefaults(
  defineProps<{
    showSearch?: boolean
    showDropdown?: boolean
    showToggle?: boolean
    searchPlaceholder?: string
    dropdownChoices?: string[]
    toggleLabel?: string
  }>(),
  {
    showSearch: true,
    showDropdown: true,
    showToggle: true,
    searchPlaceholder: 'Rechercher...',
    dropdownChoices: () => [],
    toggleLabel: 'Filtre',
  },
)

const research = defineModel<string>('research', { default: '' })
const selectedFilter = defineModel<string>('selectedFilter', { default: '' })
const isFilterActive = defineModel<boolean>('isFilterActive', { default: false })

function resetFilter() {
  research.value = ''
  selectedFilter.value = ''
  isFilterActive.value = false
}
</script>

<template>
  <div class="navbar bg-base-100 shadow-sm flex justify-around items-center gap-2 p-2">
    <BaseInput v-if="showSearch" :placeholder="searchPlaceholder" v-model:research="research" />

    <DropDown
      v-if="showDropdown"
      :dropdown-choices="dropdownChoices"
      v-model:dropdown-selection="selectedFilter"
    />

    <ToggleBtn v-if="showToggle" :label="toggleLabel" v-model:state="isFilterActive" />

    <DeleteBtn @click="resetFilter" />
  </div>
</template>

<style scoped></style>
