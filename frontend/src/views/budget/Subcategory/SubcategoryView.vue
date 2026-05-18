<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useSubcategoryStore } from '@/stores/budget/subcategoryStore.ts'
import SubcategoryTable from '@/views/budget/Subcategory/SubcategoryTable.vue'

const store = useSubcategoryStore()

onMounted(() => store.fetchAll())
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
  </div>

  <SubcategoryTable v-if="store.loading" :subcategories="store.subcategories" />
</template>

<style scoped></style>
