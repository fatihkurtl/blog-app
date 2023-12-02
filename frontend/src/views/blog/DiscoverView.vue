<script setup>
import Posts from '../../components/contents/Posts.vue';
import PostCards from '../../components/contents/PostCards.vue';
import Aside from '../../layouts/Aside.vue';
import Banner from '../../layouts/Banner.vue';
import Pagination from '../../layouts/Pagination.vue';
</script>

<template>
    <main class="container mx-auto mt-4 lg:px-0 min-w-full"> <!-- px-4 -->
        <!-- <Banner /> -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <!-- Blog Posts -->

            <!-- Posts  -->
            <!-- <Posts /> -->
            <PostCards />
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