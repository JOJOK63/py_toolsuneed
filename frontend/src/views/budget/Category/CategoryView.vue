<script setup lang="ts">
import { onMounted } from 'vue'
import { useCategoryStore } from '@/stores/budget/categoryStore'
import CategoryTable from './CategoryTable.vue'
import CategoryForm from './CategoryForm.vue'
import type { CategoryCreate } from '@/api/modules/budget/category'

const store = useCategoryStore()

onMounted(() => store.fetchAll())

// Ces fonctions reçoivent les événements des enfants et appellent le store
async function handleCreate(data: CategoryCreate) {
  await store.create(data)
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

    <div v-if="store.error" class="alert alert-error">
      <span>{{ store.error }}</span>
      <button class="btn btn-sm btn-ghost" @click="store.clearError()">✕</button>
    </div>

    <!-- On passe les données via :categories (prop) -->
    <!-- On écoute les événements via @delete, @update (emits) -->
    <CategoryTable
      v-if="!store.loading"
      :categories="store.categories"
      @delete="handleDelete"
      @update="handleUpdate"
    />

    <!-- CategoryForm remonte @submit avec les données -->
    <CategoryForm @submit="handleCreate" />
  </div>
</template>
