<script setup lang="ts">
import CreateBtn from '@/components/shared/Btn/CreateBtn.vue'
import { ref } from 'vue'
import type { TRANSACTION_TYPES } from '@/api/modules/budget/transactionTypes.ts'
import type { Subcategory } from '@/api/modules/budget/subcategory.ts'

const showToast = ref(false)
const newName = ref('')
const newAmount = ref(0)
const newDetail = ref('')
const selectedTypeId = ref('')
const selectedSubcategoryId = ref('')

const props = defineProps<{
  error?: string | null
  subcategories: Subcategory[]
  transactionTypes: typeof TRANSACTION_TYPES
}>()

console.log(props.subcategories)
function handleSubmit() {
  alert('a faire')
}
</script>

<template>
  <form @submit.prevent="handleSubmit" class="w-full">
    <fieldset class="fieldset bg-base-200 border-base-300 rounded-box border p-4">
      <legend class="fieldset-legend">Nouvelle transaction</legend>
      <label class="label">Nom</label>
      <input
        v-model="newName"
        type="text"
        class="input"
        placeholder="Nom de la transaction"
        required
      />
      <label class="label">Montant</label>
      <input
        v-model="newAmount"
        type="number"
        step="any"
        class="input"
        placeholder="Montant de la transaction"
        required
      />
      <label class="label">Détail</label>
      <input
        v-model="newDetail"
        type="text"
        class="input"
        placeholder="Détails sur la transaction"
        required
      />

      <label class="label">Type de dépenses</label>
      <select v-model="selectedTypeId" class="select" required>
        <option disabled>Choisir une catégorie</option>
        <option
          v-for="transactionType in props.transactionTypes"
          :key="transactionType.value"
          :value="transactionType.value"
        >
          {{ transactionType.label }}
        </option>
      </select>
      <label class="label">Sous catégorie</label>
      <select v-model="selectedSubcategoryId" class="select" required>
        <option disabled>Choisir une sous catégorie</option>
        <option
          v-for="subcategory in props.subcategories"
          :key="subcategory.id"
          :value="subcategory.name"
        >
          {{ subcategory.name }}
        </option>
      </select>
      <CreateBtn />
    </fieldset>
  </form>

  <!-- Toast — positionné en bas à droite, disparaît après 3s -->
  <div class="toast toast-end toast-bottom z-50">
    <div v-if="showToast" class="alert alert-error">
      <span>{{ props.error }}</span>
    </div>
  </div>
</template>

<style scoped></style>
