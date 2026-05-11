<script setup lang="ts">
import ThemeSelectorC from '@/components/shared/Navbar/ThemeSelectorC.vue'
import { RouterLink } from 'vue-router'

import { ref } from 'vue'

const menuOpen = ref(false)

function closeMenu() {
  menuOpen.value = false
}
</script>

<template>
  <div class="navbar bg-base-100 shadow-sm">
    <div class="flex">
      <a class="btn btn-ghost text-xl">ToolsUneed</a>
    </div>

    <div class="navbar-center hidden lg:flex flex-1">
      <ul class="menu menu-horizontal px-1">
        <li>
          <details :open="menuOpen" @toggle="menuOpen = ($event.target as HTMLDetailsElement).open">
            <summary>Menu</summary>
            <ul class="p-2 bg-base-100 w-40 z-1">
              <li>
                <RouterLink to="/" @click="closeMenu" :class="{ active: $route.path === '/' }">
                  Accueil
                </RouterLink>
              </li>
              <li>
                <RouterLink
                  to="/budget"
                  @click="closeMenu"
                  :class="{ active: $route.path.startsWith('/budget') }"
                >
                  Budget
                </RouterLink>
              </li>
            </ul>
          </details>
        </li>
      </ul>
    </div>

    <div class="flex gap-2">
      <ThemeSelectorC></ThemeSelectorC>

      <input type="text" placeholder="Recherche" class="input input-bordered w-24 md:w-auto" />
      <div class="dropdown dropdown-end">
        <div tabindex="0" role="button" class="btn btn-ghost btn-circle avatar">
          <div class="w-10 rounded-full">
            <img
              alt="Tailwind CSS Navbar component"
              src="https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.webp"
            />
          </div>
        </div>
        <ul
          tabindex="-1"
          class="menu menu-sm dropdown-content bg-base-100 rounded-box z-1 mt-3 w-52 p-2 shadow"
        >
          <li>
            <a class="justify-between"> Profile </a>
          </li>
          <li><a>Options</a></li>
          <li><a>Deconnection</a></li>
        </ul>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
