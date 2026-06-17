<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useSubcategoryStore } from '@/stores/budget/subcategoryStore.ts'
import SubcategoryTable from '@/views/budget/Subcategory/SubcategoryTable.vue'
import CancelBtn from '@/components/shared/Btn/CancelBtn.vue'
import type { SubcategoryCreate } from '@/api/modules/budget/subcategory.ts'
import SubcategoryForm from '@/views/budget/Subcategory/SubcategoryForm.vue'
import { useCategoryStore } from '@/stores/budget/categoryStore.ts'

const store = useSubcategoryStore()
const storeCategory = useCategoryStore()
const modalOpen = ref(false)

onMounted(() => {
  store.fetchAll()
  storeCategory.fetchAll()
})

async function handleCreate(data: SubcategoryCreate) {
  await store.create(data)
  if (!store.error) modalOpen.value = false
}

async function handleDelete(id: number) {
  await store.remove(id)
}
</script>

<template>
  <div class="p-6 flex flex-col items-center gap-6">
    <h1 class="text-2xl font-bold">Sous catégories</h1>

    <div v-if="store.loading">Chargement...</div>

    <SubcategoryTable
      v-if="!store.loading"
      :subcategories="store.subcategories"
      :categories="storeCategory.categories"
      @delete="handleDelete"
      @open-modal="modalOpen = true"
    />

    <!-- MODALE -->
    <dialog :open="modalOpen" class="modal">
      <div class="modal-box">
        <SubcategoryForm
          @submit="handleCreate"
          :categories="storeCategory.categories"
          :openModal="modalOpen"
        />
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

<style scoped></style>
