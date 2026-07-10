<script setup lang="ts">
import ThemeSelectorC from '@/components/shared/Navbar/ThemeSelectorC.vue'
import { useRoute, useRouter } from 'vue-router'
import { ref, computed, watch } from 'vue'
import NavbarBudget from '@/components/budget/NavbarBudget.vue'
import NavbarTodolist from '@/components/todolist/NavbarTodolist.vue'
import { useAuthStore } from '@/stores/auth.ts'

const route = useRoute()
const router = useRouter()
const authStore = useAuthStore()

// Ref directe sur l'élément <details>, plus fiable qu'un querySelector global
const detailsRef = ref<HTMLDetailsElement | null>(null)

function closeMenu() {
  if (detailsRef.value) {
    detailsRef.value.open = false
  }
}

// Ferme le menu automatiquement à chaque changement de route
// → règle le souci de navbar qui ne se met pas à jour après navigation
watch(
  () => route.path,
  () => {
    closeMenu()
  },
)

const currentApp = computed(() => {
  if (route.path.startsWith('/budget')) return 'budget'
  if (route.path.startsWith('/todolist')) return 'todolist'
  return 'home'
})

function handleLogout() {
  authStore.logout()
  router.push('/login')
}
</script>

<template>
  <div class="navbar bg-base-100 shadow-sm justify-between">
    <div class="flex navbar-start">
      <RouterLink to="/" class="btn btn-ghost text-xl">ToolsUneed</RouterLink>
      <div class="">
        <ul class="menu menu-horizontal px-1">
          <li>
            <details ref="detailsRef">
              <summary>
                {{
                  currentApp === 'budget'
                    ? 'Budget'
                    : currentApp === 'todolist'
                      ? 'Todolist'
                      : 'Menu'
                }}
              </summary>

              <ul class="p-2 bg-base-100 w-40 z-1">
                <template v-if="currentApp === 'home'">
                  <li>
                    <RouterLink to="/" @click="closeMenu" :class="{ active: route.path === '/' }">
                      Accueil
                    </RouterLink>
                  </li>
                  <li>
                    <RouterLink to="/budget" @click="closeMenu"> Budget </RouterLink>
                  </li>
                  <li>
                    <RouterLink to="/test" @click="closeMenu"> Test </RouterLink>
                  </li>
                  <li>
                    <RouterLink to="/todolist" @click="closeMenu"> Todolist </RouterLink>
                  </li>
                </template>

                <template v-else-if="currentApp === 'budget'">
                  <NavbarBudget :on-close="closeMenu" />
                </template>

                <template v-else-if="currentApp === 'todolist'">
                  <NavbarTodolist :on-close="closeMenu" />
                </template>
              </ul>
            </details>
          </li>
        </ul>
      </div>
    </div>

    <div class="navbar-end flex gap-6">
      <ThemeSelectorC />

      <div class="dropdown dropdown-end">
        <div tabindex="0" role="button" class="btn btn-ghost btn-circle avatar">
          <div class="w-10 rounded-full">
            <img
              alt="Avatar"
              src="https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.webp"
            />
          </div>
        </div>
        <ul
          tabindex="-1"
          class="menu menu-sm dropdown-content bg-base-100 rounded-box z-1 mt-3 w-52 p-2 shadow"
        >
          <li><a class="justify-between">Profil</a></li>
          <li><a>Options</a></li>
          <li v-if="authStore.isAuthenticated">
            <a @click="handleLogout">Déconnexion</a>
          </li>
          <li v-else>
            <RouterLink to="/login">Connexion</RouterLink>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>
