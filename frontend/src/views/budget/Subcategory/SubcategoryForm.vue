<script setup lang="ts">
import type { SubcategoryCreate } from '@/api/modules/budget/subcategory'
import { computed, ref } from 'vue'
import CreateBtn from '@/components/shared/Btn/CreateBtn.vue'
import type { Category } from '@/api/modules/budget/category.ts'

const emit = defineEmits<{
  submit: [data: SubcategoryCreate]
}>()

const newName = ref('')
const newIcon = ref<File | null>(null)
const category = ref('category')

// TODO a regarder plus en détail pour comprendre et axtiver
// Avec computed — se recalcule automatiquement quand selectedId change
// const filteredSubcategories = computed(() =>
//   store.subcategories.filter((s) => s.category === selectedId.value),
// )

function handleIconChange(event: Event) {
  const input = event.target as HTMLInputElement
  newIcon.value = input.files?.[0] ?? null
}

function handleSubmit() {
  if (!newName.value.trim()) return
  emit('submit', {
    name: newName.value,
    icon: newIcon.value,
    // todo injecter liste de cateegorie pour assigner la bonne
    category: 0,
  })
  newName.value = ''
  newIcon.value = null
  category.value = ''
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
      <input type="file" accept="image/*" class="file-input" @change="handleIconChange" />
      <CreateBtn @click="handleSubmit()" />
    </fieldset>
  </form>
</template>

<style scoped></style>
