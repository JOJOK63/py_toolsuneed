<script setup lang="ts">
import type { SubcategoryCreate } from '@/api/modules/budget/subcategory'
import type { Category } from '@/api/modules/budget/category'
import { ref } from 'vue'
import CreateBtn from '@/components/shared/Btn/CreateBtn.vue'

const props = defineProps<{
  categories: Category[]
  openModal: boolean
}>()

const emit = defineEmits<{
  submit: [data: SubcategoryCreate]
}>()

const newName = ref('')
const newIcon = ref<File | null>(null)
const category = ref('category')
const selectedCategoryId = ref<number | null>(null)
const fileInput = ref<HTMLInputElement | null>(null)

function handleIconChange(event: Event) {
  const input = event.target as HTMLInputElement
  newIcon.value = input.files?.[0] ?? null
}

function handleSubmit() {
  if (newName.value.trim() && newIcon.value && selectedCategoryId.value) {
    emit('submit', {
      name: newName.value,
      icon: newIcon.value,
      category: selectedCategoryId.value,
    })
    newName.value = ''
    newIcon.value = null
    category.value = ''

    if (fileInput.value) {
      fileInput.value.value = ''
    }

    !props.openModal
  }
}
</script>

<template>
  <form @submit.prevent="handleSubmit" class="w-full">
    <fieldset class="fieldset bg-base-200 border-base-300 rounded-box border p-4">
      <legend class="fieldset-legend">Nouvelle catégorie</legend>
      <label class="label">Nom</label>
      <input
        v-model="newName"
        type="text"
        class="input"
        placeholder="Nom de la catégorie"
        required
      />
      <label class="label">Icône</label>
      <input
        type="file"
        ref="fileInput"
        accept="image/*"
        class="file-input"
        @change="handleIconChange"
        required
      />
      <label class="label">Catégorie</label>
      <select v-model="selectedCategoryId" class="select" required>
        <option disabled :value="null">Choisir une catégorie</option>
        <option v-for="category in props.categories" :key="category.id" :value="category.id">
          {{ category.name }}
        </option>
      </select>
      <CreateBtn @click="handleSubmit()" />
    </fieldset>
  </form>
</template>

<style scoped></style>
