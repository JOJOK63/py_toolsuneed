<script setup lang="ts">
import type { SubcategoryCreate } from '@/api/modules/budget/subcategory'
import { ref } from 'vue'
import CreateBtn from '@/components/shared/Btn/CreateBtn.vue'

const emit = defineEmits<{
  submit: [data: SubcategoryCreate]
}>()

const newName = ref('')
const newIcon = ref<File | null>(null)

function handleSubmit() {
  if (!newName.value.trim()) return
  emit('submit', { name: newName.value, icon: newIcon.value })
  newName.value = ''
  newIcon.value = null
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
      <input type="file" accept="image/*" class="file-input" />
      <CreateBtn />
    </fieldset>
  </form>
</template>

<style scoped></style>
