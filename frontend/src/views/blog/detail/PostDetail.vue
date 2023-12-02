<script setup>
import { ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useFetch } from '../../../composables/services/post.get';
import Aside from '../../../layouts/Aside.vue';
import CommentSection from '../../../components/details/CommentSection.vue';
import Actions from '../../../components/contents/Actions.vue';
import Articles from '../../../layouts/Articles.vue';
import DetailSkeleton from '../../../components/skeletons/DetailSkeleton.vue';

const route = useRoute();
console.log(`slug: ${route.params.slug}`);


const { response, loading, error } = useFetch('/products');


</script>

<template>
    <main class="container mx-auto mt-4 px-4 lg:px-0 min-w-full">
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <div class="col-span-2">
                <div class="overflow-hidden mb-6 flex flex-col md:flex-row">
                    <!-- Blog Post -->
                    <Actions />
                    <div class="p-6 mt-8">
                    <DetailSkeleton v-if="loading && !error" />
                        <h1 v-if="!loading && !error" class="text-2xl font-bold dark:text-white mb-4">Blog Post Title {{ route.params.slug }}</h1>
                        <p v-if="!loading && !error" class="dark:text-white text-gray-900 font-sans">Lorem ipsum dolor sit amet, consectetur
                            adipisicing elit. Distinctio
                            dolorum doloribus earum expedita facere harum, hic itaque molestiae nam nemo
                            perferendis quam quibusdam ratione
                            recusandae sequi similique temporibus totam voluptas.
                        </p>
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
        <Articles />

    </main>
</template>

<style lang="scss" scoped></style>