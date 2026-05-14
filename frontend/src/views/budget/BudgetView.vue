<script setup lang="ts"></script>

<template>
  <div class="w-full min-h-screen">
    <!-- Cet en-tête reste toujours visible quand on est dans /budget/* -->
    <div class="bg-base-200 p-4">
      <h1 class="text-xl font-bold">💰 Budget Application</h1>
    </div>

    <!-- Ici s'affiche CategoryView ou SubcategoryView selon la route -->
    <RouterView />
  </div>
</template>
