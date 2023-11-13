<script setup>
import { ref } from 'vue';
import Success from '../notifications/comment/Success.vue';
import Failure from '../notifications/comment/Failure.vue';

const showCommentSuccess = ref(false);
const showCommentFailure = ref(false);

const save = () => { // comment basarili olursa diye bir ornek, ayni islem basarisiz sonuclar icin showCommentFailure ile de yapilacak
    showCommentSuccess.value = true;

    setTimeout(() => {
        showCommentSuccess.value = false;

    }, 5000);
};
</script>

<template>
    <div class="bg-lightItemsColor dark:bg-darkItemsColor p-6 mt-8">
        <!-- Comment -->
        <RouterLink to="/user/:slug" class="flex items-start">
            <img src="https://via.placeholder.com/64" alt="User Avatar" class="w-8 h-8 rounded-full mr-4">
            <div class="border border-neutral-200 dark:border-neutral-800 rounded-lg px-4 py-2">
                <h2 class="text-base font-semibold dark:text-white text-black">John Doe</h2>
                <p class="text-sm dark:text-white hyphens-auto text-black font-sans">
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sodales ex ipsum, at dapibus mi blandit a.
                </p>
            </div>
        </RouterLink>
        <!-- Comment -->

        <!-- Comment -->
        <div class="flex items-start mt-4">
            <img src="https://via.placeholder.com/64" alt="User Avatar" class="w-8 h-8 rounded-full mr-4">
            <RouterLink to="/user/:slug">
            <div class="border border-neutral-200 dark:border-neutral-800 rounded-lg px-4 py-2">
                <h2 class="text-base font-semibold dark:text-white text-black">Jane Smith</h2>
                <p class="text-sm dark:text-white hyphens-auto text-black font-sans">
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sodales ex ipsum, at dapibus mi blandit a.
                </p>
            </div>
            </RouterLink>
        </div>
        <!-- Comment -->

        <!-- Yorum olmadigi zaman gozukecek alan -->
        <!-- <div class="mt-4 dark:text-white text-sm text-center">
            <p class="text-black dark:text-white font-semibold">{{$t('no-comments-yet')}}</p>
            <p class="text-gray-500 dark:text-gray-400">{{$t('be-the-first-to-comment')}}</p>
        </div> -->
        <!-- Yorum olmadigi zaman gozukecek alan -->

        <!-- Comment Form -->
        <!-- Yorum basariyla yapildiginda gozukecek -->
        <div class="my-8">
            <Success :showCommentSuccess="showCommentSuccess" />
        </div>
        <!-- Yorum basariyla yapildiginda gozukecek -->
        <!-- Yorum basarisiz yapildiginda gozukecek -->
        <div class="my-8">
            <Failure :showCommentFailure="showCommentFailure" />
        </div>
        <!-- Yorum basarisiz yapildiginda gozukecek -->
        <!-- <form class="mt-8" @submit.prevent="save">
            <div class="flex">
                <img src="https://via.placeholder.com/64" alt="User Avatar" class="w-8 h-8 rounded-full mr-4">
                <textarea
                    class="resize-none w-full h-24 py-2 px-4 border dark:bg-darkBgColor dark:text-white text-gray-600 border-gray-500 rounded-lg focus:outline-none focus:border-gray-300"
                    :placeholder="$t('comment-placeholder')" />
            </div>
            <button type="submit"
                class="dark:bg-darkBtnColor dark:hover:bg-sky-700 bg-lightBtnColor hover:bg-sky-600 text-white font-semibold py-2 px-4 rounded-lg mt-4 text-center">
                {{ $t('send') }}
            </button>
        </form> -->
        <!-- Comment Form -->

        <!-- Kullanici register veya login olmadiginda cikacak comment form -->
        <div class="relative">
            <form class="mt-8 blur opacity-50">
                <div class="flex items-center mb-4">
                    <img src="https://via.placeholder.com/64" alt="User Avatar" class="w-8 h-8 rounded-full mr-4">
                    <textarea
                        class="resize-none w-full h-24 py-2 px-4 border dark:bg-darkBgColor dark:text-white text-black border-gray-500 rounded-lg focus:outline-none focus:border-gray-300 pointer-events-none"
                        :placeholder="$t('comment-placeholder')"></textarea>
                </div>
                <button type="submit"
                    class="dark:bg-darkBtnColor dark:hover:bg-sky-700 bg-lightBtnColor hover:bg-sky-600 text-white font-semibold py-2 px-4 rounded-lg mt-4 text-center pointer-events-none">
                    {{ $t('send') }}
                </button>
            </form>
            <div class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-center">
                <RouterLink to="/register"
                    class="font-sans dark:text-white text-black underline hover:text-sky-500 dark:hover:text-sky-500">
                    {{ $t('register') }}</RouterLink>
                <span class="mx-2 font-sans dark:text-white text-black">{{ $t('or') }}</span>
                <RouterLink to="/login"
                    class="font-sans dark:text-white text-black underline hover:text-sky-500 dark:hover:text-sky-500">
                    {{ $t('login') }}</RouterLink>
            </div>
        </div>
        <!-- Kullanici register veya login olmadiginda cikacak comment form -->
    </div>
</template>

<style lang="scss" scoped></style>