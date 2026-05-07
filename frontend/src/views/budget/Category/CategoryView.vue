<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useCategoryStore } from '@/stores/budget/categoryStore.ts'

const store = useCategoryStore()

const newName = ref('')
const newColor = ref('#000000')
const newIcon = ref<File | null>(null)

const editingId = ref<number | null>(null)
const editingName = ref('')
const editingColor = ref('')
const editingIcon = ref<File | null>(null)

onMounted(() => store.fetchAll())

function handleNewIconChange(event: Event) {
  const input = event.target as HTMLInputElement
  newIcon.value = input.files?.[0] ?? null
}

function handleEditIconChange(event: Event) {
  const input = event.target as HTMLInputElement
  editingIcon.value = input.files?.[0] ?? null
}

async function handleCreate() {
  if (!newName.value.trim()) return
  await store.create({ name: newName.value, color: newColor.value, icon: newIcon.value })
  newName.value = ''
  newColor.value = '#000000'
  newIcon.value = null
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

async function handleUpdate() {
  if (!editingName.value.trim() || editingId.value === null) return
  await store.update(editingId.value, {
    name: editingName.value,
    color: editingColor.value,
    icon: editingIcon.value,
  })
  cancelEdit()
}

async function handleDelete(id: number) {
  await store.remove(id)
}
</script>

<template>
  <div class="p-6 flex flex-col items-center gap-6">
    <h1 class="text-2xl font-bold">Catégories</h1>

    <div v-if="store.loading">Chargement...</div>
    <div v-else-if="store.error" class="alert alert-error">{{ store.error }}</div>

    <!-- TABLEAU -->
    <div v-else class="overflow-x-auto w-3/4 bg-base-200 border-base-300 rounded-box border p-4">
      <table class="table flex ">
        <thead>
          <tr>
            <th>Icône</th>
            <th>Nom</th>
            <th>Couleur</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="category in store.categories" :key="category.id">
            <!-- MODE ÉDITION -->
            <template v-if="editingId === category.id">
              <td>
                <input type="file" accept="image/*" @change="handleEditIconChange" />
              </td>
              <td>
                <input v-model="editingName" class="input input-bordered input-sm" />
              </td>
              <td>
                <input v-model="editingColor" type="color" />
              </td>
              <td class="flex gap-2 bg-warning">
                <button class="btn btn-success btn-sm" @click="handleUpdate">Sauvegarder</button>
                <button class="btn btn-ghost btn-sm" @click="cancelEdit">Annuler</button>
              </td>
            </template>

            <!-- MODE AFFICHAGE -->
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
              <td class="">
                <button
                  class="btn btn-ghost btn-sm"
                  @click="startEdit(category.id, category.name, category.color)"
                >
                  Modifier
                </button>
                <button class="btn btn-error btn-sm" @click="handleDelete(category.id)">
                  Supprimer
                </button>
              </td>
            </template>
          </tr>
        </tbody>
      </table>
    </div>

<!--  Create form a mettre dans un autre component  -->
    <form @submit.prevent="handleCreate" class="w-1/2">
      <fieldset class="fieldset bg-base-200 border-base-300 rounded-box border p-4">
        <legend class="fieldset-legend">Nouvelle catégorie</legend>

        <label class="label">Nom</label>
        <input v-model="newName" type="text" class="input" placeholder="Nom de la catégorie" />

        <label class="label">Couleur</label>
        <input v-model="newColor" type="color" class="h-12 w-16 cursor-pointer rounded border" />

        <label class="label">Icône</label>
        <input type="file" accept="image/*" class="file-input" @change="handleNewIconChange" />

        <button class="btn btn-primary mt-2" type="submit">Créer</button>
      </fieldset>
    </form>
  </div>
</template>
