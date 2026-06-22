<script setup lang="ts">
import ToggleBtn from '@/components/shared/Btn/ToggleBtn.vue'
import { ref } from 'vue'
import BaseInput from '@/components/shared/BaseInput.vue'
import DropDown from '@/components/shared/DropDown.vue'

/// For toggle filter
const isFilterActive = ref<boolean>(false)

//For input research
const placeholder = ref<string>('Rechercher...')
const research = ref<string>('')

//for Dropdown filter
const listParamFilter = ref<string[]>(['Option 1', 'Option 2', 'Option 3'])
const selectedFilter = ref<string>('')
</script>

<template>
  <div class="navbar bg-base-100 shadow-sm flex justify-around items-center gap-2 p-2">
    <BaseInput :placeholder="placeholder" v-model:research="research"></BaseInput>
    <p>Recherche actuelle: {{ research }}</p>

    <DropDown
      v-model:dropdown-choices="listParamFilter"
      v-model:dropdown-selection="selectedFilter"
    ></DropDown>
    <p>Filtre actif ? {{ isFilterActive ? 'Oui' : 'Non' }}</p>

    <ToggleBtn label="mon filtre" v-model:state="isFilterActive"></ToggleBtn>
  </div>
</template>

<style scoped></style>
