<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useSubcategoryStore } from '@/stores/budget/subcategoryStore.ts'
import SubcategoryTable from '@/views/budget/Subcategory/SubcategoryTable.vue'
import CancelBtn from '@/components/shared/Btn/CancelBtn.vue'
import type { SubcategoryCreate } from '@/api/modules/budget/subcategory.ts'
import SubcategoryForm from '@/views/budget/Subcategory/SubcategoryForm.vue'

const store = useSubcategoryStore()
const modalOpen = ref(false)

onMounted(() => store.fetchAll())

async function handleCreate(data: SubcategoryCreate) {
  await store.create(data)
  if (!store.error) modalOpen.value = false
}
</script>

<template>
  <div class="p-6 flex flex-col items-center gap-6">
    <h1 class="text-2xl font-bold">Sous catégories</h1>

    <div v-if="store.loading">Chargement...</div>

    <!-- Erreur de chargement uniquement -->
    <div v-if="store.error" class="alert alert-error">
      <span>{{ store.error }}</span>
      <button class="btn btn-sm btn-ghost" @click="store.clearError()">✕</button>
    </div>

    <SubcategoryTable
      v-if="!store.loading"
      :subcategories="store.subcategories"
      @open-modal="modalOpen = true"
    />

    <!-- MODALE -->
    <dialog :open="modalOpen" class="modal">
      <div class="modal-box">
        <SubcategoryForm :error="store.error" @submit="handleCreate" />
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
