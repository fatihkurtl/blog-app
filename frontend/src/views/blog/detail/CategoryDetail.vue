<script setup>
import Aside from '../../../layouts/Aside.vue';
import CommentSection from '../../../components/details/CommentSection.vue';
import { useRoute, useRouter } from 'vue-router';

const route = useRoute()
console.log(`id: ${route.params.id} - category: ${route.params.category}`);
</script>

<template>
    <main class="container mx-auto mt-4 px-4 lg:px-0">
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <div class="col-span-2">
                <div class="bg-lightItemsColor dark:bg-darkItemsColor overflow-hidden mb-6 flex flex-col md:flex-row">
                    <!-- Blog Post -->
                    <div class="dark:bg-darkItemsColor p-6 mt-8">
                        <h1 class="text-2xl font-bold dark:text-white mb-4">Blog Post Title {{ route.params.id }}</h1>
                        <p class="dark:text-white text text-black font-sans">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Distinctio
                            dolorum
                            doloribus
                            earum
                            expedita facere harum, hic itaque molestiae nam nemo perferendis quam quibusdam ratione
                            recusandae
                            sequi
                            similique temporibus totam voluptas.</p>
                        <!-- Comment Section -->
                        <CommentSection />
                        <!-- Comment Section -->
                    </div>

                </div>
            </div>
            <!--Aside-->
            <Aside />
            <!--Aside-->
        </div>
    </main>
</template>

<style lang="scss" scoped></style>