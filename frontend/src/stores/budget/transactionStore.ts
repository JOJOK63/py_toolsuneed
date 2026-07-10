import { defineStore } from 'pinia'
import { fetchTransactionApi, type Transaction } from '@/api/modules/budget/transaction.ts'
import { ref } from 'vue'
import { TRANSACTION_TYPES } from '@/api/modules/budget/transactionTypes.ts'

export const useTransactionStore = defineStore('transactionStore', () => {
  const transactions = ref<Transaction[]>([])
  const loading = ref<boolean>(false)
  const error = ref<string | null>(null)
  const transactionsTypes = TRANSACTION_TYPES
  const isFilterActive = ref(false)

  async function fetchAll() {
    loading.value = true
    error.value = null
    try {
      transactions.value = await fetchTransactionApi.getAll()
    } catch (e) {
      error.value = 'Impossible de charger les transactions'
    } finally {
      loading.value = false
    }
  }

  return { transactions, loading, error, transactionsTypes, isFilterActive, fetchAll }
})
