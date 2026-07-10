import api from '@/api'
import type { TransactionType } from '@/api/modules/budget/transactionTypes.ts'
import type { Subcategory } from '@/api/modules/budget/subcategory.ts'

// Forme réelle reçue après conversion camelCase (dates encore en string ISO)
interface TransactionDto {
  id: number
  name: string
  amount: string
  detail: string
  transactionType: TransactionType
  createdAt: string
  updatedAt: string
  budget: number
  subcategory: number | null
  subcategoryDetail: Subcategory | null
}

// Modèle utilisé côté front
export interface Transaction {
  id: number
  name: string
  amount: string
  detail: string
  transactionType: TransactionType
  createdAt: Date
  updatedAt: Date
  budget: number
  subcategory: number | null
  subcategoryDetail: Subcategory | null
}

function adaptTransaction(dto: TransactionDto): Transaction {
  return {
    ...dto,
    createdAt: new Date(dto.createdAt),
    updatedAt: new Date(dto.updatedAt),
  }
}

export const fetchTransactionApi = {
  async getAll() {
    const response = await api.get<TransactionDto[]>('/budget/financial-transaction')
    return response.data.map(adaptTransaction)
  },
}
