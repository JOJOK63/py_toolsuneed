import api from '@/api'
import type { TransactionType } from '@/api/modules/budget/transactionTypes.ts'

export interface Transaction {
  id: number
  name: string
  amount: string
  detail: string
  transactionType: TransactionType
  createdAt: Date
  updatedAt: Date
  // budget: number
  // subcategory: number | null
}

export const fetchTransactionApi = {
  getAll() {
    return api.get<Transaction[]>('/budget/financial-transaction')
  },
}
