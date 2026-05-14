<script setup lang="ts">
import ThemeSelectorC from '@/components/shared/Navbar/ThemeSelectorC.vue'
import { useRoute } from 'vue-router'
import { ref, computed, onMounted, onUnmounted } from 'vue'
import NavbarBudget from '@/components/budget/NavbarBudget.vue'

const route = useRoute()
const menuOpen = ref(false)

function closeMenu() {
  menuOpen.value = false
}

function handleClickOutside(event: MouseEvent) {
  const target = event.target as HTMLElement
  if (!target.closest('details')) {
    menuOpen.value = false
  }
}

// Au montage du composant → on écoute les clics sur TOUT le document
onMounted(() => {
  document.addEventListener('click', handleClickOutside)
})

// Au démontage → on retire l'écouteur pour éviter les fuites mémoire
onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside)
})

// can change and make an adaptive bar, just add route path here
const currentApp = computed(() => {
  if (route.path.startsWith('/budget')) return 'budget'
  return 'home'
})
</script>

<template>
  <div class="navbar bg-base-100 shadow-sm" @click="handleClickOutside">
    <div class="flex">
      <RouterLink to="/" class="btn btn-ghost text-xl">ToolsUneed</RouterLink>
    </div>

    <div class="navbar-center lg:flex flex-1">
      <ul class="menu menu-horizontal px-1">
        <li>
          <details :open="menuOpen" @toggle="menuOpen = ($event.target as HTMLDetailsElement).open">
            <!-- Le titre du menu change selon l'app -->
            <summary>{{ currentApp === 'budget' ? 'Budget' : 'Menu' }}</summary>

            <ul class="p-2 bg-base-100 w-40 z-1">
              <!-- Menu HOME -->
              <template v-if="currentApp === 'home'">
                <li>
                  <RouterLink to="/" @click="closeMenu" :class="{ active: route.path === '/' }">
                    Accueil
                  </RouterLink>
                </li>
                <li>
                  <RouterLink to="/budget" @click="closeMenu"> Budget </RouterLink>
                </li>
              </template>

              <!-- Menu BUDGET -->
              <template v-else-if="currentApp === 'budget'">
                <NavbarBudget :on-close="closeMenu" />
              </template>
            </ul>
          </details>
        </li>
      </ul>
    </div>

    <div class="flex gap-2">
      <ThemeSelectorC />
      <input type="text" placeholder="Recherche" class="input input-bordered w-24 md:w-auto" />
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
          <li><a>Déconnexion</a></li>
        </ul>
      </div>
    </div>
  </div>
</template>
