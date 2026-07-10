import { defineStore } from 'pinia'
import { fetchTransactionApi, type Transaction } from '@/api/modules/budget/transaction.ts'
import { ref } from 'vue'
import { TRANSACTION_TYPES, type TransactionType } from '@/api/modules/budget/transactionTypes.ts'

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
      const response = await fetchTransactionApi.getAll()

      // On type explicitement "item: any" ou le type brut de ton API pour le map
      transactions.value = response.data.map((item: any) => ({
        // 1. On garde toutes les propriétés existantes (id, name, amount, detail, budget...)
        ...item,

        // 2. On renomme et on mappe ce qui doit l'être en camelCase
        transactionType: item.transaction_type,

        // 3. On convertit les chaînes de texte de l'API en vrais objets Date attendus par ton interface
        createdAt: new Date(item.created_at),
        updatedAt: new Date(item.updated_at),

        // 4. On adapte la sous-catégorie pour qu'elle corresponde à ton interface
        subcategory: item.subcategory_detail,
      }))
      console.log(transactions.value)
    } catch (e) {
      error.value = 'Impossible de charger les transactions'
    } finally {
      loading.value = false
    }
  }

  return { transactions, loading, error, transactionsTypes, fetchAll }
})
