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
  <div class="container mx-auto px-4 md:container md:mx-auto dark:bg-darkBgColor">
    <header>
      <Navbar />
    </header>
    <RouterView />
    <Footer />
  </div>
</template>

<style scoped></style>
