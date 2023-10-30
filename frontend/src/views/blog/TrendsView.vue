<script setup>
import Posts from '../../components/contents/Posts.vue';
import Aside from '../../layouts/Aside.vue';
import Pagination from '../../layouts/Pagination.vue';
</script>

<template>
    <main class="container mx-auto mt-4 px-4 lg:px-0">
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <!-- Blog Posts -->

            <!-- Posts  -->
            <Posts />
            <!-- Posts  -->

            <!-- Aside -->
            <Aside />
            <!-- Aside -->
        </div>

        <!-- Pagination -->
        <Pagination />
        <!-- Pagination -->

    </main>
</template>

<style scoped></style>