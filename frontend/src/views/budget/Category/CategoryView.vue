<!-- CategoryView.vue -->
<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import { useCategoryStore } from '@/stores/budget/categoryStore'
import CategoryTable from './CategoryTable.vue'
import CategoryForm from './CategoryForm.vue'
import type { CategoryCreate } from '@/api/modules/budget/category'
import CancelBtn from '@/components/shared/Btn/CancelBtn.vue'
import FilterBar from '@/components/shared/Bar/FilterBar.vue'

const store = useCategoryStore()
const modalOpen = ref(false)

const search = ref('')

const filteredCategories = computed(() => {
  let result = [...store.categories]

  if (search.value) {
    result = result.filter((s) => s.name.toLowerCase().includes(search.value.toLowerCase()))
  }

  return result
})

onMounted(() => store.fetchAll())

async function handleCreate(data: CategoryCreate) {
  await store.create(data)
  // Ferme la modale seulement si pas d'erreur
  if (!store.error) modalOpen.value = false
}

async function handleUpdate(id: number, data: Partial<CategoryCreate>) {
  await store.update(id, data)
}

async function handleDelete(id: number) {
  await store.remove(id)
}
</script>

<template>
  <div class="p-6 flex flex-col items-center gap-6">
    <h1 class="text-2xl font-bold">Catégories</h1>

    <div v-if="store.loading">Chargement...</div>

    <!-- Erreur de chargement uniquement -->
    <div v-if="store.error && !modalOpen" class="alert alert-error">
      <span>{{ store.error }}</span>
      <button class="btn btn-sm btn-ghost" @click="store.clearError()">✕</button>
    </div>

    <FilterBar
      :show-toggle="false"
      :show-dropdown="false"
      search-placeholder="Rechercher une catégorie"
      v-model:research="search"
    ></FilterBar>

    <CategoryTable
      v-if="!store.loading"
      :categories="filteredCategories"
      @delete="handleDelete"
      @update="handleUpdate"
      @open-modal="modalOpen = true"
    />

    <!-- MODALE -->
    <dialog :open="modalOpen" class="modal">
      <div class="modal-box">
        <CategoryForm :error="store.error" @submit="handleCreate" />
        <CancelBtn @click="modalOpen = false" />
      </div>
      <form
        method="dialog"
        class="modal-backdrop"
        @click="((modalOpen = false), store.clearError())"
      ></form>
    </dialog>
  </div>
</template>
