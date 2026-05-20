<script setup lang="ts">
import { ref } from 'vue'
import type { Category, CategoryCreate } from '@/api/modules/budget/category'
import AddBtn from '@/components/shared/Btn/AddBtn.vue'
import SaveBtn from '@/components/shared/Btn/SaveBtn.vue'
import CancelBtn from '@/components/shared/Btn/CancelBtn.vue'
import EditBtn from '@/components/shared/Btn/EditBtn.vue'
import DeleteBtn from '@/components/shared/Btn/DeleteBtn.vue'

// defineProps = données que le PARENT envoie à ce composant
// Le parent passe :categories="store.categories"
const props = defineProps<{
  categories: Category[]
}>()

// defineEmits = événements que ce composant envoie AU PARENT
const emit = defineEmits<{
  delete: [id: number]
  update: [id: number, data: Partial<CategoryCreate>]
  openModal: [] // ← nouvel emit
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
          <th class="flex items-center gap-3">
            <p>Actions</p>
            <AddBtn @click="emit('openModal')" />
          </th>
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
                <SaveBtn @click="handleUpdate" />
                <CancelBtn @click="cancelEdit" />
              </div>
            </td>
          </template>

          <template v-else>
            <td>
              <div class="mask mask-squircle h-10 w-10" :style="{ background: category.color }">
                <img
                  v-if="category.icon"
                  :src="category.icon"
                  class="h-10 w-10 p-1"
                  :alt="`icone de la ${category.name}`"
                />
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
              <div class="flex gap-5">
                <EditBtn @click="startEdit(category.id, category.name, category.color)" />
                <DeleteBtn @click="handleDelete(category.id)" />
              </div>
            </td>
          </template>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped></style>
