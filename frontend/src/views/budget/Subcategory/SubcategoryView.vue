<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useCategoryStore } from '@/stores/budget/categoryStore'
import CategoryTable from './CategoryTable.vue'
import CategoryForm from './CategoryForm.vue'
import type { CategoryCreate } from '@/api/modules/budget/category'
import CancelBtn from '@/components/shared/Btn/CancelBtn.vue'
import TableCrud from '@/components/shared/TableCrud.vue'

const store = useCategoryStore()
const modalOpen = ref(false)

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
  <TableCrud :entities="store.categories" />
</template>

<style scoped></style>
