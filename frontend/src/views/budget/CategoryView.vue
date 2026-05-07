<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useCategoryStore } from '@/stores/budget/categoryStore'

const store = useCategoryStore()

// --- CRÉATION ---
const newName = ref('')
const newColor = ref('#000000')
const newIcon = ref<File | null>(null)

// --- ÉDITION ---
const editingId = ref<number | null>(null)
const editingName = ref('')
const editingColor = ref('')
const editingIcon = ref<File | null>(null)

onMounted(() => {
  store.fetchAll()
})

// Quand l'utilisateur choisit un fichier dans l'input file de création
function handleNewIconChange(event: Event) {
  const input = event.target as HTMLInputElement
  // input.files[0] = le premier fichier sélectionné
  newIcon.value = input.files?.[0] ?? null
}

// Quand l'utilisateur choisit un fichier dans l'input file d'édition
function handleEditIconChange(event: Event) {
  const input = event.target as HTMLInputElement
  editingIcon.value = input.files?.[0] ?? null
}

// --- CRÉATION ---
async function handleCreate() {
  if (!newName.value.trim()) return

  await store.create({
    name: newName.value,
    color: newColor.value,
    icon: newIcon.value,
  })
  // Remet tout à zéro après création
  newName.value = ''
  newColor.value = '#000000'
  newIcon.value = null
}

// --- ÉDITION ---
function startEdit(id: number, currentName: string, currentColor: string) {
  editingId.value = id
  editingName.value = currentName
  editingColor.value = currentColor
  editingIcon.value = null // l'icône ne change que si l'utilisateur en choisit une nouvelle
}

function cancelEdit() {
  editingId.value = null
  editingName.value = ''
  editingColor.value = ''
  editingIcon.value = null
}

async function handleUpdate() {
  if (!editingName.value.trim()) return
  if (editingId.value === null) return

  await store.update(editingId.value, {
    name: editingName.value,
    color: editingColor.value,
    icon: editingIcon.value,
  })

  editingId.value = null
  editingName.value = ''
  editingColor.value = ''
  editingIcon.value = null
}

// --- SUPPRESSION ---
async function handleDelete(id: number) {
  await store.remove(id)
}
</script>

<template>
  <div>
    <h1>Catégories</h1>

    <div v-if="store.loading">Chargement...</div>
    <div v-else-if="store.error">{{ store.error }}</div>

    <ul v-else>
      <li v-for="category in store.categories" :key="category.id">
        <!-- Mode édition pour CETTE catégorie -->
        <div v-if="editingId === category.id">
          <input v-model="editingName" placeholder="Nom" />
          <input v-model="editingColor" type="color" />
          <!-- input type="file" ne fonctionne pas avec v-model → on écoute @change -->
          <input type="file" accept="image/*" @change="handleEditIconChange" />
          <button @click="handleUpdate">Sauvegarder</button>
          <button @click="cancelEdit">Annuler</button>
        </div>

        <!-- Mode affichage normal -->
        <div v-else>
          <!-- Affiche l'icône si elle existe -->
          <img v-if="category.icon" :src="category.icon" width="32" height="32" />
          <span :style="{ color: category.color }">{{ category.name }}</span>
          <button @click="startEdit(category.id, category.name, category.color)">Modifier</button>
          <button @click="handleDelete(category.id)">Supprimer</button>
        </div>
      </li>
    </ul>

    <!-- Formulaire de création -->
    <form @submit.prevent="handleCreate">
      <input v-model="newName" placeholder="Nom de la catégorie" />
      <input v-model="newColor" type="color" />
      <input type="file" accept="image/*" @change="handleNewIconChange" />
      <button type="submit">Créer</button>
    </form>
  </div>
</template>
