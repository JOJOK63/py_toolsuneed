<script setup lang="ts">
import { ref } from 'vue'
import type { CategoryCreate } from '@/api/modules/budget/category'

// defineEmits = déclare les événements que ce composant peut envoyer au parent
// 'submit' est le nom de l'événement
// [data: CategoryCreate] est le type de ce qu'on envoie
const emit = defineEmits<{
  submit: [data: CategoryCreate]
}>()

const newName = ref('')
const newColor = ref('#000000')
const newIcon = ref<File | null>(null)

function handleIconChange(event: Event) {
  const input = event.target as HTMLInputElement
  newIcon.value = input.files?.[0] ?? null
}

function handleSubmit() {
  if (!newName.value.trim()) return
  // emit('submit', data) → envoie l'événement au parent avec les données
  emit('submit', { name: newName.value, color: newColor.value, icon: newIcon.value })
  newName.value = ''
  newColor.value = '#000000'
  newIcon.value = null
}
</script>

<template>
  <form @submit.prevent="handleSubmit" class="w-1/2">
    <fieldset class="fieldset bg-base-200 border-base-300 rounded-box border p-4">
      <legend class="fieldset-legend">Nouvelle catégorie</legend>
      <label class="label">Nom</label>
      <input v-model="newName" type="text" class="input" placeholder="Nom de la catégorie" />
      <label class="label">Couleur</label>
      <input v-model="newColor" type="color" class="h-12 w-16 cursor-pointer rounded border" />
      <label class="label">Icône</label>
      <input type="file" accept="image/*" class="file-input" @change="handleIconChange" />
      <button class="btn btn-primary mt-2" type="submit">Créer</button>
    </fieldset>
  </form>
</template>
