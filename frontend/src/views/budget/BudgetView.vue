<script setup lang="ts"></script>

<template>
  <div class="w-full min-h-screen">
    <!-- Cet en-tête reste toujours visible quand on est dans /budget/* -->
    <div class="bg-base-200 p-4">
      <h1 class="text-xl font-bold flex items-center gap-2">
        <img src="/img/icons-budget-40.png" alt="" class="w-10 h-10" />
        Budget Application
      </h1>
    </div>

    <!-- Ici s'affiche CategoryView ou SubcategoryView selon la route -->
    <RouterView />
  </div>
</template>
