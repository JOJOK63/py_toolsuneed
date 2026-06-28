// TODO mettre les transactions types en mode api avec endpoint
// 1. La constante brute (valeur JavaScript qui existera à l'exécution)
export const TRANSACTION_TYPES = [
  { value: 'EXP', label: 'Dépense' },
  { value: 'INC', label: 'Revenu' },
  { value: 'TRSF', label: 'Virement' },
] as const

// 2. Le type TypeScript extrait automatiquement de la constante
// (équivaut à : 'EXP' | 'INC' | 'TRSF')
export type TransactionType = (typeof TRANSACTION_TYPES)[number]['value']
