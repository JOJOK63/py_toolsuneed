<script setup lang="ts">
import AddBtn from '@/components/shared/Btn/AddBtn.vue'
import EditBtn from '@/components/shared/Btn/EditBtn.vue'
import DeleteBtn from '@/components/shared/Btn/DeleteBtn.vue'
import type { Transaction } from '@/api/modules/budget/transaction.ts'

const props = defineProps<{
  transactions: Transaction[]
}>()

const emit = defineEmits<{
  openModal: []
}>()
</script>

<template>
  <div class="overflow-x-auto w-3/4 bg-base-200 border-base-300 rounded-box border p-4">
    <table class="table">
      <thead>
        <tr>
          <th>Nom</th>
          <th>Montant</th>
          <th>detail</th>
          <th>type</th>
          <th>Sous catégorie / catégorie</th>
          <th>créer le</th>
          <th>modifier le</th>
          <th class="flex items-center gap-3">
            <p>Actions</p>
            <AddBtn @click="emit('openModal')" />
          </th>
        </tr>
      </thead>
      <tbody>
        <!-- props.categories ou juste categories — les deux fonctionnent -->
        <tr v-for="transaction in transactions" :key="transaction.id">
          <template v-if="false">
            <!--            v-if="editingId === transaction.id">-->
            <!--            <td><input type="file" accept="image/*" @change="handleEditIconChange" /></td>-->
            <!--            <td><input v-model="editingName" class="input input-bordered input-sm" /></td>-->
            <!--            <td>-->
            <!--              <select v-model="editingCategory" class="select select-sm">-->
            <!--                <option v-for="cat in props.categories" :key="cat.id" :value="cat.id">-->
            <!--                  {{ cat.name }}-->
            <!--                </option>-->
            <!--              </select>-->
            <!--            </td>-->
            <!--            <td>-->
            <!--              <div class="flex gap-2">-->
            <!--                <SaveBtn @click="handleUpdate" />-->
            <!--                <CancelBtn @click="cancelEdit" />-->
            <!--              </div>-->
            <!--            </td>-->
          </template>

          <template v-else>
            <td class="font-bold">{{ transaction.name }}</td>
            <td class="font-bold">{{ transaction.amount }}</td>
            <td class="font-bold">{{ transaction.detail }}</td>
            <td class="font-bold">{{ transaction.transactionType }}</td>
            <td>
              {{ transaction.subcategory?.name }}
              <span>{{ transaction.subcategory?.category_detail?.name }}</span>
            </td>
            <td class="font-bold">transaction.createdAt</td>
            <td class="font-bold">{{ transaction.updatedAt }}</td>
            <td>
              <div class="flex gap-5">
                <!--                todo edit btn-->
                <EditBtn />
                <!--                todo delete btn-->
                <DeleteBtn />
              </div>
            </td>
          </template>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped></style>
