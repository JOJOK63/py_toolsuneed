<script setup lang="ts">
import { ref, watch } from 'vue'
import type { CategoryCreate } from '@/api/modules/budget/category'
import CreateBtn from '@/components/shared/Btn/CreateBtn.vue'

const props = defineProps<{
  error?: string | null
}>()

const emit = defineEmits<{
  submit: [data: CategoryCreate]
}>()

const newName = ref('')
const newColor = ref('#000000')
const newIcon = ref<File | null>(null)
const fileInput = ref<HTMLInputElement | null>(null)

const showToast = ref(false)

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
  //  si champ vide on sort on ne fait même ^pas la suite
  if (!newName.value.trim()) return
  if (!newColor.value) return
  if (!newIcon.value) return
  emit('submit', { name: newName.value, color: newColor.value, icon: newIcon.value })
  newName.value = ''
  newColor.value = '#000000'
  newIcon.value = null

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
      <label class="label">Couleur</label>
      <input v-model="newColor" type="color" class="h-12 w-16 cursor-pointer rounded border" />
      <label class="label">Icône</label>
      <input
        type="file"
        ref="fileInput"
        accept="image/*"
        class="file-input"
        @change="handleIconChange"
        required
      />
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
