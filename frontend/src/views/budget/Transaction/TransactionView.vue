<script setup lang="ts">
import TransactionTable from '@/views/budget/Transaction/TransactionTable.vue'
import { useTransactionStore } from '@/stores/budget/transactionStore.ts'
import { computed, onMounted, ref } from 'vue'

const store = useTransactionStore()
const modalOpen = ref(false)

// --- état du filtre, propre à cette page ---
//à faire

const filteredFinancialTransactions = computed(() => {
  let result = [...store.transactions]

  return result
})

onMounted(() => {
  store.fetchAll()
  storeSubcategory.fetchAll()
})
</script>

<template>
  <div class="p-6 flex flex-col items-center gap-6">
    <h1 class="text-2xl font-bold">Transactions</h1>

    <!--    TODO FILTER BAR-->

    <div v-if="store.loading">Chargement...</div>

    <TransactionTable :transactions="filteredFinancialTransactions"></TransactionTable>

    <!--    todo dialog form-->
  </div>
</template>

<style scoped></style>
