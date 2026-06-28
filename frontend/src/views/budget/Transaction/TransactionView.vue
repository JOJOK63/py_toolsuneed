<script setup lang="ts">
import TransactionTable from '@/views/budget/Transaction/TransactionTable.vue'
import TransactionForm from '@/views/budget/Transaction/TransactionForm.vue'
import { useTransactionStore } from '@/stores/budget/transactionStore.ts'

const store = useTransactionStore()
</script>

<template>
  <h1>Transaction view</h1>

  <TransactionTable></TransactionTable>

  <TransactionForm :transactionTypes="store.transactionsTypes"></TransactionForm>
</template>

<style scoped></style>
