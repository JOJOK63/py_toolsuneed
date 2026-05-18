<script setup lang="ts">
import SaveBtn from '@/components/shared/Btn/SaveBtn.vue'
import CancelBtn from '@/components/shared/Btn/CancelBtn.vue'
import DeleteBtn from '@/components/shared/Btn/DeleteBtn.vue'
import EditBtn from '@/components/shared/Btn/EditBtn.vue'
import AddBtn from '@/components/shared/Btn/AddBtn.vue'
import type { Subcategory, SubcategoryCreate } from '@/api/modules/budget/subcategory.ts'
import { ref } from 'vue'

const props = defineProps<{
  subcategories: Subcategory[]
}>()

const emit = defineEmits<{
  delete: [id: number]
  update: [id: number, data: Partial<SubcategoryCreate>]
  openModal: []
}>()

const editingId = ref<number | null>(null)
const editingName = ref('')
const editingIcon = ref<File | null>(null)
//  Todo ajouter categorie

function handleEditIconChange(event: Event) {
  const input = event.target as HTMLInputElement
  editingIcon.value = input.files?.[0] ?? null
}

function startEdit(id: number, name: string) {
  editingId.value = id
  editingName.value = name
  editingIcon.value = null
}

function cancelEdit() {
  editingId.value = null
  editingName.value = ''
  editingIcon.value = null
}

function handleUpdate() {
  if (!editingName.value.trim() || editingId.value === null) return
  // On remonte l'événement 'update' au parent avec l'id et les données
  emit('update', editingId.value, {
    name: editingName.value,
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
  <template>
    <div class="overflow-x-auto w-3/4 bg-base-200 border-base-300 rounded-box border p-4">
      <table class="table">
        <thead>
          <tr>
            <th>Icône</th>
            <th>Nom</th>
            <th>Catégorie</th>
            <th class="flex items-center gap-3">
              <p>Actions</p>
              <AddBtn @click="emit('openModal')" />
            </th>
          </tr>
        </thead>
        <tbody>
          <!-- props.categories ou juste categories — les deux fonctionnent -->
          <tr v-for="subcategory in props.subcategories" :key="subcategory.id">
            <template v-if="editingId === subcategory.id">
              <td><input type="file" accept="image/*" @change="handleEditIconChange" /></td>
              <td><input v-model="editingName" class="input input-bordered input-sm" /></td>
              <td><input type="text" /></td>
              <td>
                <div class="flex gap-2">
                  <SaveBtn @click="handleUpdate" />
                  <CancelBtn @click="cancelEdit" />
                </div>
              </td>
            </template>

            <template v-else>
              <td>
                <div
                  class="mask mask-squircle h-10 w-10"
                  :style="{ background: subcategory.category.color }"
                >
                  <img v-if="subcategory.icon" :src="subcategory.icon" class="h-10 w-10 p-1" />
                </div>
              </td>
              <td class="font-bold">{{ subcategory.name }}</td>
              <td>
                <span
                  class="inline-block w-6 h-6 rounded"
                  :style="{ backgroundColor: subcategory.category.color }"
                ></span>
              </td>
              <td>
                <div class="flex gap-5">
                  <EditBtn @click="startEdit(subcategory.id, subcategory.name, category.id)" />
                  <DeleteBtn @click="handleDelete(subcategory.id)" />
                </div>
              </td>
            </template>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
</template>

<style scoped></style>
