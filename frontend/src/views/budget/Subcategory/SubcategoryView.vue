<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import { useSubcategoryStore } from '@/stores/budget/subcategoryStore.ts'
import SubcategoryTable from '@/views/budget/Subcategory/SubcategoryTable.vue'
import CancelBtn from '@/components/shared/Btn/CancelBtn.vue'
import type { SubcategoryCreate } from '@/api/modules/budget/subcategory.ts'
import SubcategoryForm from '@/views/budget/Subcategory/SubcategoryForm.vue'
import { useCategoryStore } from '@/stores/budget/categoryStore.ts'
import FilterBar from '@/components/shared/Bar/FilterBar.vue'

const store = useSubcategoryStore()
const storeCategory = useCategoryStore()
const modalOpen = ref(false)

// --- état du filtre, propre à cette page ---
const search = ref('')
const selectedCategory = ref('')
const sortByCategory = ref(false)

const categoryNames = computed(() => storeCategory.categories.map((c) => c.name))

const filteredSubcategories = computed(() => {
  let result = [...store.subcategories]

  if (search.value) {
    result = result.filter((s) => s.name.toLowerCase().includes(search.value.toLowerCase()))
  }

  if (selectedCategory.value) {
    result = result.filter((s) => s.category_detail?.name === selectedCategory.value)
  }

  if (sortByCategory.value) {
    result.sort((a, b) =>
      (a.category_detail?.name || '').localeCompare(b.category_detail?.name || ''),
    )
  }

  return result
})

onMounted(() => {
  store.fetchAll()
  storeCategory.fetchAll()
})

async function handleCreate(data: SubcategoryCreate) {
  await store.create(data)
  if (!store.error) modalOpen.value = false
}

async function handleUpdate(id: number, data: Partial<SubcategoryCreate>) {
  await store.update(id, data)
}

async function handleDelete(id: number) {
  await store.remove(id)
}
</script>

<template>
  <div class="p-6 flex flex-col items-center gap-6">
    <h1 class="text-2xl font-bold">Sous catégories</h1>

    <FilterBar
      search-placeholder="Rechercher une sous-catégorie..."
      :dropdown-choices="categoryNames"
      toggle-label="Trier par catégorie"
      v-model:research="search"
      v-model:selectedFilter="selectedCategory"
      v-model:isFilterActive="sortByCategory"
    />

    <div v-if="store.loading">Chargement...</div>

    <SubcategoryTable
      v-if="!store.loading"
      :subcategories="filteredSubcategories"
      :categories="storeCategory.categories"
      @delete="handleDelete"
      @update="handleUpdate"
      @open-modal="modalOpen = true"
    />

    <!-- MODALE -->
    <dialog :open="modalOpen" class="modal">
      <div class="modal-box">
        <SubcategoryForm
          :error="store.error"
          @submit="handleCreate"
          :categories="storeCategory.categories"
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
