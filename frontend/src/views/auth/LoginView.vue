<script setup lang="ts">
import { ref } from 'vue'
import CreateBtn from '@/components/shared/Btn/CreateBtn.vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth.ts'

const router = useRouter()
const authStore = useAuthStore()
const username = ref('')
const password = ref('')

const handleLogin = async () => {
  const success = await authStore.login({ username: username.value, password: password.value })
  if (success) {
    router.push('/') // ou ta route post-login
  }
}
</script>

<template>
  <div class="min-h-[calc(100vh-4rem)] flex items-center justify-center">
    <form @submit.prevent="handleLogin">
      <fieldset class="fieldset bg-base-200 border-base-300 rounded-box w-xs border p-4">
        <legend class="fieldset-legend">Login</legend>

        <label class="label">Nom</label>
        <input type="text" class="input" placeholder="Email" v-model="username" required />

        <label class="label">Mot de passe</label>
        <input type="password" class="input" placeholder="Password" v-model="password" required />

        <p v-if="authStore.error" class="text-error text-sm">{{ authStore.error }}</p>

        <CreateBtn label="Connexion"></CreateBtn>
      </fieldset>
    </form>
  </div>
</template>
