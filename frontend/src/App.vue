<script setup>
import { ref } from 'vue';
import Navbar from './layouts/Navbar.vue';
import Footer from './layouts/Footer.vue';
import { baseApi } from './composables/api/baseApi';

console.log(`App.vue => ${baseApi('eeee')}`);

console.log(import.meta.env.VITE_APP_MODE);  // 'development' veya 'production'
console.log(import.meta.env.VITE_API_BASE_URL);  // API base URL

</script>

<template>
  <div class="container min-h-screen min-w-full mx-auto px-4 md:container md:mx-auto dark:bg-darkBgColor"> <!-- px-4 -->
    <header>
      <Navbar />
    </header>
    <RouterView class="router-view" v-slot="{ Component }">
      <Transition name="page-opacity" mode="out-in">
        <component :is="Component"/>
      </Transition>
    </RouterView>
    <Footer />
  </div>
</template>

<style>
.page-opacity-enter-active,
.page-opacity-leave-active {
  transition: 600ms ease all;
}

.page-opacity-enter-from,
.page-opacity-leave-to {
  opacity: 0;
}
</style>
