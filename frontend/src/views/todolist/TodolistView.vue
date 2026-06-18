<script setup lang="ts">
import { computed, ref } from 'vue'
import { Status } from '@/api/modules/status.ts'
import { Priority } from '@/api/modules/priority.ts'
import DeleteBtn from '@/components/shared/Btn/DeleteBtn.vue'
import AddBtn from '@/components/shared/Btn/AddBtn.vue'

const showAddModal = ref(false)
const todolist = ref([
  {
    id: 1,
    name: 'todo 1',
    detail: 'todo 1 detail',
    state: Status.TODO,
    priority: Priority.LOW,
  },
  {
    id: 2,
    name: 'todo 2',
    detail: 'todo 2 detail',
    state: Status.IN_PROGRESS,
    priority: Priority.MEDIUM,
  },
  {
    id: 3,
    name: 'todo 3',
    detail: 'todo 3 detail',
    state: Status.DONE,
    priority: Priority.HIGH,
  },
  {
    id: 4,
    name: 'todo 4',
    detail: 'todo 4 detail',
    state: Status.DONE,
    priority: Priority.HIGH,
  },
])
const nextId = ref(todolist.value.length + 1)
const todolistByStatus = computed(() => {
  return {
    [Status.TODO]: todolist.value.filter((t) => t.state === Status.TODO),
    [Status.IN_PROGRESS]: todolist.value.filter((t) => t.state === Status.IN_PROGRESS),
    [Status.DONE]: todolist.value.filter((t) => t.state === Status.DONE),
  }
})
const newTodo = ref({
  name: '',
  detail: '',
  state: Status.TODO,
  priority: Priority.LOW,
})

function addTodolist() {
  todolist.value.push({ id: nextId.value++, ...newTodo.value })
  // reset form
  newTodo.value = { name: '', detail: '', state: Status.TODO, priority: Priority.LOW }
  if (todolist.value.length != nextId.value) {
    showAddModal.value = false
  }
}

function deleteTodo(id: number) {
  todolist.value = todolist.value.filter((t) => t.id !== id)
}
</script>

<template>
  <div class="w-full min-h-screen flex flex-col items-center">
    <div class="bg-base-200 p-4 w-full">
      <h1 class="text-xl font-bold flex items-center gap-2">
        <img src="/img/icons-taches-64.png" alt="" class="w-10 h-10" />
        Todolist Application
      </h1>
    </div>

    <AddBtn
      v-if="!showAddModal"
      type="submit"
      class="m-4"
      @click="showAddModal = !showAddModal"
    ></AddBtn>

    <form v-if="showAddModal" @submit.prevent="addTodolist">
      <fieldset class="fieldset bg-base-200 border-base-300 rounded-box w-xs border p-4 my-4">
        <legend class="fieldset-legend">Todo ajout</legend>

        <label class="label capitalize" for="nom">nom</label>
        <input id="nom" type="text" class="input" v-model="newTodo.name" required minlength="2" />

        <label class="label capitalize" for="detail">détail</label>
        <input id="detail" type="text" class="input" v-model="newTodo.detail" required />

        <label class="label capitalize">priorité</label>
        <select class="select" v-model="newTodo.priority">
          <option v-for="priority in Priority" :key="priority" :value="priority">
            {{ priority }}
          </option>
        </select>
        <AddBtn type="submit">Ajouter</AddBtn>
      </fieldset>
    </form>

    <div
      class="w-full min-h-screen p-8 grid grid-cols-1 md:grid-cols-3 lg:grid-cols-3 gap-x-10 items-start"
    >
      <div v-for="state in Status" :key="state" class="border rounded-md p-2">
        <h1 class="text-center uppercase py-2">{{ state }}</h1>
        <div class="overflow-x-auto">
          <table class="table">
            <thead>
              <tr>
                <th>Tâche</th>
                <th>Détails</th>
                <th>Priorité</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              <template v-if="todolistByStatus[state].length > 0">
                <tr v-for="todo in todolistByStatus[state]" :key="todo.id">
                  <td>{{ todo.name }}</td>
                  <td>{{ todo.detail }}</td>
                  <td>{{ todo.priority }}</td>
                  <td>
                    <DeleteBtn @click="deleteTodo(todo.id)"></DeleteBtn>
                  </td>
                </tr>
              </template>
              <tr v-else>
                <td colspan="4">Il n'y a pas de tâches</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <RouterView />
  </div>
</template>
