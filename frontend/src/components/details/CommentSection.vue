<script setup>
import { ref } from 'vue';
import Success from '../notifications/comment/Success.vue';
import Failure from '../notifications/comment/Failure.vue';

const showCommentSuccess = ref(false);
const showCommentFailure = ref(false);

// const save = () => { // comment basarili olursa diye bir ornek, ayni islem basarisiz sonuclar icin showCommentFailure ile de yapilacak
//     showCommentSuccess.value = true;

//     setTimeout(() => {
//         showCommentSuccess.value = false;

//     }, 5000);
// };
</script>

<template>
    <div class="p-6 mt-8">
        <div class="flex justify-between items-center mb-6">
                  <h2 class="text-lg lg:text-2xl font-bold text-gray-900 dark:text-white">{{ $t('comments') }}</h2>
              </div>
        <!-- Commnet Form -->
        <form class="mb-6">
            <!-- <div
                class="py-2 px-4 mb-4 bg-white rounded-lg rounded-t-lg border border-gray-200 dark:bg-darkBgColor dark:border-gray-700"> -->
                <!-- <label for="comment" class="text-gray-600 dark:text-white">{{ $t('comment-placeholder') }}</label> -->
                <textarea id="comment" rows="6"
                    class="py-2 px-4 mb-4 w-full text-sm font-sans font-medium text-gray-900 border-gray-300 dark:border-gray-600 rounded-lg bg-lightItemsColor focus:ring-blue-500 focus:border-blue-500 dark:focus:ring-blue-500 dark:focus:border-blue-500 placeholder-gray-400 dark:text-white dark:placeholder-gray-400 dark:bg-darkBgColor"
                    :placeholder="$t('comment-placeholder')" required></textarea>
            <!-- </div> -->
            <button type="submit"
                class="inline-flex items-center py-2.5 px-4 text-xs text-center dark:bg-darkBtnColor dark:hover:bg-sky-700 bg-lightBtnColor hover:bg-sky-600 text-white font-semibold rounded-lg focus:ring-4 focus:ring-primary-200 dark:focus:ring-primary-900 hover:bg-primary-800">
                {{ $t('send') }}
            </button>
        </form>
        <!-- Commnet Form -->
        <!-- Comment -->
        <article
            class="p-6 mb-6 text-base rounded-lg border-t border-gray-200 dark:border-gray-700 bg-lightItemsColor dark:bg-darkItemsColor">
            <footer class="flex justify-between items-center mb-2">
                <div class="flex items-center">
                    <RouterLink :to="{ name: 'Visitor Profile', params: { 'username': 'bonnie_green'}, query: {'name': 'Bonnie Green'} }" class="inline-flex items-center mr-3 font-semibold text-sm text-gray-900 dark:text-white"><img
                            class="mr-2 w-6 h-6 rounded-full"
                            src="https://flowbite.com/docs/images/people/profile-picture-3.jpg" alt="Bonnie Green">
                            Bonnie Green
                        </RouterLink>
                    <p class="text-sm text-gray-600 dark:text-gray-400"><time pubdate datetime="2022-03-12"
                            title="March 12th, 2022">Mar. 12, 2022</time></p>
                </div>
                <button id="dropdownComment3Button" data-dropdown-toggle="dropdownComment3"
                    class="inline-flex items-center p-2 text-sm font-medium text-center text-gray-600 dark:text-gray-400 rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-gray-50 bg-lightItemsColor dark:bg-darkItemsColor dark:hover:bg-gray-700 dark:focus:ring-gray-600"
                    type="button">
                    <svg class="w-4 h-4" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor"
                        viewBox="0 0 16 3">
                        <path
                            d="M2 0a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3Zm6.041 0a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM14 0a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3Z" />
                    </svg>
                    <span class="sr-only">Comment settings</span>
                </button>
                <!-- Dropdown menu -->
                <div id="dropdownComment3"
                    class="hidden z-10 w-36 bg-white rounded divide-y divide-gray-100 shadow dark:bg-gray-700 dark:divide-gray-600">
                    <ul class="py-1 text-sm text-gray-700 dark:text-gray-200"
                        aria-labelledby="dropdownMenuIconHorizontalButton">
                        <li>
                            <a href="#"
                                class="block py-2 px-4 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Report</a>
                        </li>
                    </ul>
                </div>
            </footer>
            <p class="text-gray-600 dark:text-white">
                The article covers the essentials, challenges, myths and stages the UX designer should consider while
                creating the design strategy.
            </p>
            <!-- <div class="flex items-center mt-4 space-x-4">
                <button type="button"
                    class="flex items-center font-medium text-sm text-gray-600 hover:underline dark:text-gray-400">
                    <svg class="mr-1.5 w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor"
                        viewBox="0 0 20 18">
                        <path
                            d="M18 0H2a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h2v4a1 1 0 0 0 1.707.707L10.414 13H18a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2Zm-5 4h2a1 1 0 1 1 0 2h-2a1 1 0 1 1 0-2ZM5 4h5a1 1 0 1 1 0 2H5a1 1 0 0 1 0-2Zm2 5H5a1 1 0 0 1 0-2h2a1 1 0 0 1 0 2Zm9 0h-6a1 1 0 0 1 0-2h6a1 1 0 1 1 0 2Z" />
                    </svg>
                    Reply
                </button>
            </div> -->
        </article>
        <article
            class="p-6 text-base rounded-lg border-t border-gray-200 dark:border-gray-700 bg-lightItemsColor dark:bg-darkItemsColor">
            <footer class="flex justify-between items-center mb-2">
                <div class="flex items-center">
                    <RouterLink :to="{ name: 'Visitor Profile', params: { 'username': 'helene_engels'}, query: {'name': 'Helene Engels'} }" class="inline-flex items-center mr-3 font-semibold text-sm text-gray-900 dark:text-white"><img
                            class="mr-2 w-6 h-6 rounded-full"
                            src="https://flowbite.com/docs/images/people/profile-picture-4.jpg" alt="Helene Engels">
                            Helene Engels
                    </RouterLink>
                    <p class="text-sm text-gray-600 dark:text-gray-400"><time pubdate datetime="2022-06-23"
                            title="June 23rd, 2022">Jun. 23, 2022</time></p>
                </div>
                <button id="dropdownComment4Button" data-dropdown-toggle="dropdownComment4"
                    class="inline-flex items-center p-2 text-sm font-medium text-center text-gray-500 rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-gray-50 dark:text-gray-400 bg-lightItemsColor dark:bg-darkItemsColor dark:hover:bg-gray-700 dark:focus:ring-gray-600"
                    type="button">
                    <svg class="w-4 h-4" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor"
                        viewBox="0 0 16 3">
                        <path
                            d="M2 0a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3Zm6.041 0a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM14 0a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3Z" />
                    </svg>
                </button>
                <!-- Dropdown menu -->
                <div id="dropdownComment4"
                    class="hidden z-10 w-36 bg-white rounded divide-y divide-gray-100 shadow dark:bg-gray-700 dark:divide-gray-600">
                    <ul class="py-1 text-sm text-gray-700 dark:text-gray-200"
                        aria-labelledby="dropdownMenuIconHorizontalButton">
                        <li>
                            <a href="#"
                                class="block py-2 px-4 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Report</a>
                        </li>
                    </ul>
                </div>
            </footer>
            <p class="text-gray-600 dark:text-white">
                Thanks for sharing this. I do came from the Backend development and explored some of the tools to design my
                Side Projects.
            </p>
            <!-- <div class="flex items-center mt-4 space-x-4">
                <button type="button"
                    class="flex items-center font-medium text-sm text-gray-500 hover:underline dark:text-gray-400">
                    <svg class="mr-1.5 w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor"
                        viewBox="0 0 20 18">
                        <path
                            d="M18 0H2a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h2v4a1 1 0 0 0 1.707.707L10.414 13H18a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2Zm-5 4h2a1 1 0 1 1 0 2h-2a1 1 0 1 1 0-2ZM5 4h5a1 1 0 1 1 0 2H5a1 1 0 0 1 0-2Zm2 5H5a1 1 0 0 1 0-2h2a1 1 0 0 1 0 2Zm9 0h-6a1 1 0 0 1 0-2h6a1 1 0 1 1 0 2Z" />
                    </svg>
                    Reply
                </button>
            </div> -->
        </article>
        <!-- Comment -->

        <!-- Comment -->
        <!-- <div class="flex items-start mt-4"> -->
        <!-- <RouterLink to="/user/:slug" class="flex items-start mt-4">
            <img src="https://via.placeholder.com/64" alt="User Avatar" class="w-8 h-8 rounded-full mr-2">
            <div
                class="border border-gray-300 dark:border-gray-700 hover:border-gray-400 dark:hover:border-gray-500 rounded-lg px-4 py-2">
                <h2 class="text-base font-semibold dark:text-white text-black">Jane Smith</h2>
                <p class="text-sm dark:text-white hyphens-auto text-black font-sans">
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sodales ex ipsum, at dapibus mi blandit a.
                </p>
            </div>
        </RouterLink> -->
        <!-- </div> -->
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
        <!-- <div class="relative">
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
        </div> -->
        <!-- Kullanici register veya login olmadiginda cikacak comment form -->
    </div>
</template>

<style lang="scss" scoped></style>