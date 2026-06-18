<script setup lang="ts">
import type { SubcategoryCreate } from '@/api/modules/budget/subcategory'
import type { Category } from '@/api/modules/budget/category'
import { ref, watch } from 'vue'
import CreateBtn from '@/components/shared/Btn/CreateBtn.vue'

const props = defineProps<{
  categories: Category[]
  error?: string | null
}>()

const emit = defineEmits<{
  submit: [data: SubcategoryCreate]
}>()

const newName = ref('')
const newIcon = ref<File | null>(null)
const selectedCategoryId = ref<number | null>(null)
const fileInput = ref<HTMLInputElement | null>(null)

// Toast local
const showToast = ref(false)

// Quand l'erreur change → affiche le toast
watch(
  () => props.error,
  (newError) => {
    if (newError) {
      showToast.value = true
      setTimeout(() => {
        showToast.value = false
      }, 3000)
    } else {
      // Si l'erreur est effacée → cache le toast immédiatement
      showToast.value = false
    }
  },
)
function handleIconChange(event: Event) {
  const input = event.target as HTMLInputElement
  newIcon.value = input.files?.[0] ?? null
}

function handleSubmit() {
  if (!newName.value.trim()) return
  if (!newIcon.value) return
  if (!selectedCategoryId.value) return
  emit('submit', {
    name: newName.value,
    icon: newIcon.value,
    category: selectedCategoryId.value,
  })
  newName.value = ''
  newIcon.value = null
  selectedCategoryId.value = null // tu avais oublié de reset celui-là aussi

  if (fileInput.value) {
    fileInput.value.value = ''
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
        <option disabled>Choisir une catégorie</option>
        <option v-for="category in props.categories" :key="category.id" :value="category.id">
          {{ category.name }}
        </option>
      </select>
      <CreateBtn />
    </fieldset>
  </form>

  <!-- Toast — positionné en bas à droite, disparaît après 3s -->
  <div class="toast toast-end toast-bottom z-50">
    <div v-if="showToast" class="alert alert-error">
      <span>{{ props.error }}</span>
    </div>
  </div>
</template>

<style scoped></style>
