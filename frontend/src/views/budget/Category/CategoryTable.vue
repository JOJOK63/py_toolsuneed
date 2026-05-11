<script setup lang="ts">
import { ref } from 'vue'
import type { Category, CategoryCreate } from '@/api/modules/budget/category'

// defineProps = données que le PARENT envoie à ce composant
// Le parent passe :categories="store.categories"
const props = defineProps<{
  categories: Category[]
}>()

// defineEmits = événements que ce composant envoie AU PARENT
const emit = defineEmits<{
  delete: [id: number]
  update: [id: number, data: Partial<CategoryCreate>]
}>()

// L'état d'édition reste LOCAL à ce composant — le parent n'en a pas besoin
const editingId = ref<number | null>(null)
const editingName = ref('')
const editingColor = ref('')
const editingIcon = ref<File | null>(null)

function handleEditIconChange(event: Event) {
  const input = event.target as HTMLInputElement
  editingIcon.value = input.files?.[0] ?? null
}

function startEdit(id: number, name: string, color: string) {
  editingId.value = id
  editingName.value = name
  editingColor.value = color
  editingIcon.value = null
}

function cancelEdit() {
  editingId.value = null
  editingName.value = ''
  editingColor.value = ''
  editingIcon.value = null
}

function handleUpdate() {
  if (!editingName.value.trim() || editingId.value === null) return
  // On remonte l'événement 'update' au parent avec l'id et les données
  emit('update', editingId.value, {
    name: editingName.value,
    color: editingColor.value,
    icon: editingIcon.value,
  })
  cancelEdit()
}

function handleDelete(id: number) {
  // On remonte l'événement 'delete' au parent avec l'id
  emit('delete', id)
}
</script>

<template>
  <div class="overflow-x-auto w-3/4 bg-base-200 border-base-300 rounded-box border p-4">
    <table class="table">
      <thead>
        <tr>
          <th>Icône</th>
          <th>Nom</th>
          <th>Couleur</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <!-- props.categories ou juste categories — les deux fonctionnent -->
        <tr v-for="category in props.categories" :key="category.id">
          <template v-if="editingId === category.id">
            <td><input type="file" accept="image/*" @change="handleEditIconChange" /></td>
            <td><input v-model="editingName" class="input input-bordered input-sm" /></td>
            <td><input v-model="editingColor" type="color" /></td>
            <td>
              <div class="flex gap-2">
                <button class="btn btn-success btn-sm" @click="handleUpdate">Sauvegarder</button>
                <button class="btn btn-ghost btn-sm" @click="cancelEdit">Annuler</button>
              </div>
            </td>
          </template>

          <template v-else>
            <td>
              <div class="mask mask-squircle h-10 w-10" :style="{ background: category.color }">
                <img v-if="category.icon" :src="category.icon" class="h-10 w-10" />
              </div>
            </td>
            <td class="font-bold">{{ category.name }}</td>
            <td>
              <span
                class="inline-block w-6 h-6 rounded"
                :style="{ backgroundColor: category.color }"
              ></span>
            </td>
            <td>
              <div class="flex gap-2">
                <button
                  class="btn btn-primary btn-outline btn-sm"
                  @click="startEdit(category.id, category.name, category.color)"
                >
                  Modifier
                </button>
                <button class="btn btn-error btn-outline btn-sm" @click="handleDelete(category.id)">
                  Supprimer
                </button>
              </div>
            </td>
          </template>
        </tr>
      </tbody>
    </table>
  </div>
</template>
