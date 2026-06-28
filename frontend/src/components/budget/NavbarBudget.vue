<!-- NavbarBudget.vue -->
<script setup lang="ts">
import { useRoute } from 'vue-router'

const route = useRoute()

// NavbarBudget reçoit closeMenu du parent via props
const props = defineProps<{
  onClose: () => void
}>()
</script>

<template>
  <li>
    <RouterLink to="/budget" @click="props.onClose" :class="{ active: route.path === '/budget' }">
      Budgets
    </RouterLink>
  </li>
  <li>
    <RouterLink
      to="/budget/categories"
      @click="props.onClose"
      :class="{ active: route.path === '/budget/categories' }"
    >
      Catégories
    </RouterLink>
  </li>
  <li>
    <RouterLink
      to="/budget/subcategories"
      @click="props.onClose"
      :class="{ active: route.path === '/budget/subcategories' }"
    >
      Sous-catégories
    </RouterLink>
  </li>
  <li>
    <RouterLink
      to="/budget/transactions"
      @click="props.onClose"
      :class="{ active: route.path === '/budget/subcategories' }"
    >
      Transactions
    </RouterLink>
  </li>
</template>
