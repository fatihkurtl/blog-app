<script setup>
import Aside from '../../../../components/members/auth/Aside.vue';
</script>

<template>
    <main class="container mx-auto mt-4 min-w-full lg:px-0"> <!-- px-4 -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">

            <!-- Content -->
            <div class="col-span-2">
                <div class="bg-lightItemsColor dark:bg-darkItemsColor overflow-hidden mb-6 flex flex-col md:flex-row">
                    <!-- <img src="https://via.placeholder.com/400x300" alt="Blog Post Image"
                        class="w-full md:w-1/3 h-auto object-cover"> -->
                    <div class="w-full md:w-2/3 p-4">
                        <h2 class="text-xl md:text-2xl font-sans font-semibold text-black dark:text-white mb-2">
                            Account
                        </h2>
                        <p class="text-gray-800 font-sans dark:text-gray-300 mb-2">Lorem ipsum dolor sit amet, consectetur
                            adipiscing
                            elit. Vivamus quis porta dui. Ut eu iaculis massa.</p>
                        <!-- <RouterLink :to="(route.fullPath === '/') ? '/post_detail/1' : '/post_detail' + route.fullPath + '/1'"
                    class="text-blue-500 hover:underline">{{ $t('read-more') }}</RouterLink> -->
                    </div>
                </div>

            </div>
            <!-- Content -->

            <!-- Aside -->
            <Aside />
            <!-- Aside -->
        </div>
        <br>
    </main>
</template>

<style lang="scss" scoped></style>