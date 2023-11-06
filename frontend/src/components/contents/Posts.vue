<script setup>
import { useRoute, useRouter } from 'vue-router';
const route = useRoute();
console.log(route.fullPath);
</script>

<template>
    <!-- Blog Post 1 -->
    <div class="col-span-2">
        <div class="bg-lightItemsColor dark:bg-darkItemsColor overflow-hidden mb-6 flex flex-col md:flex-row">
            <img src="https://via.placeholder.com/400x300" alt="Blog Post Image"
                class="w-full md:w-1/3 h-auto object-cover">
            <div class="w-full md:w-2/3 p-4">
                <h2 class="text-xl md:text-2xl font-sans font-semibold text-black dark:text-white mb-2">Blog Post Title 1
                </h2>
                <p class="text-gray-800 font-sans dark:text-gray-300 mb-2">Lorem ipsum dolor sit amet, consectetur
                    adipiscing
                    elit. Vivamus quis porta dui. Ut eu iaculis massa.</p>
                <RouterLink :to="(route.fullPath === '/') ? '/blog-post-1' : route.fullPath + '/blog-post-1'"
                    class="text-blue-500 hover:underline">{{ $t('read-more') }}</RouterLink>
            </div>
        </div>

        <!-- Blog Post 2 -->
        <div class="bg-lightItemsColor dark:bg-darkItemsColor overflow-hidden mb-6 flex flex-col md:flex-row">
            <img src="https://via.placeholder.com/400x300" alt="Blog Post Image"
                class="w-full md:w-1/3 h-auto object-cover">
            <div class="w-full md:w-2/3 p-4">
                <h2 class="text-xl md:text-2xl font-sans font-semibold text-black dark:text-white mb-2">Blog Post Title 2
                </h2>
                <p class="text-gray-800 font-sans dark:text-gray-300 mb-2">Lorem ipsum dolor sit amet, consectetur
                    adipiscing
                    elit. Vivamus quis porta dui. Ut eu iaculis massa.</p>
                <RouterLink :to="(route.fullPath === '/') ? '/blog-post-2' : route.fullPath + '/blog-post-2'"
                    class="text-blue-500 hover:underline">{{ $t('read-more') }}</RouterLink>
            </div>
        </div>

        <!-- Blog Post 3 -->
        <div class="bg-lightItemsColor dark:bg-darkItemsColor overflow-hidden mb-6 flex flex-col md:flex-row">
            <img src="https://via.placeholder.com/400x300" alt="Blog Post Image"
                class="w-full md:w-1/3 h-auto object-cover">
            <div class="w-full md:w-2/3 p-4">
                <h2 class="text-xl md:text-2xl font-sans font-semibold text-black dark:text-white mb-2">Blog Post Title 3
                </h2>
                <p class="text-gray-800 font-sans dark:text-gray-300 mb-2">Lorem ipsum dolor sit amet, consectetur
                    adipiscing
                    elit. Vivamus quis porta dui. Ut eu iaculis massa.</p>
                <RouterLink :to="(route.fullPath === '/') ? '/blog-post-3' : route.fullPath + '/blog-post-3'"
                    class="text-blue-500 hover:underline">{{ $t('read-more') }}</RouterLink>
            </div>
        </div>
    </div>
</template>

<style lang="scss" scoped></style>