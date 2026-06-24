<script setup lang="ts">
import { ref } from 'vue'
import CreateBtn from '@/components/shared/Btn/CreateBtn.vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const username = ref('')
const password = ref('')
const errorMessage = ref('')
const showPassword = ref(false)

const handleLogin = async () => {
  errorMessage.value = ''

  try {
    const response = await fetch('http://localhost:8000/api/login/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username: username.value,
        password: password.value,
      }),
    })
    if (response.ok) {
      const data = await response.json()
      console.log('Login successfull', data)
      localStorage.setItem('access', data.access)
      localStorage.setItem('refresh', data.refresh)
    } else {
      const errorData = await response.json()
      console.log('error data', errorData)
    }
  } catch (error) {
    console.log('Error', error)
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

        <CreateBtn label="Connexion"></CreateBtn>
      </fieldset>
    </form>
  </div>
</template>

<style scoped></style>
