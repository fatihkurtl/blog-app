<script setup>
import { useRoute, useRouter } from 'vue-router';


const route = useRoute();
</script>

<template>
    <section class="col-span-2">
        <ul class="grid grid-cols-1 xl:grid-cols-3 gap-y-10 gap-x-6 items-start">
            <RouterLink :to="(route.fullPath === '/') ? '/blog-post-1' : route.fullPath + '/blog-post-1'"
                class="relative flex flex-col sm:flex-row xl:flex-col items-start border border-gray-300 dark:border-gray-700 hover:border-gray-400 dark:hover:border-gray-500 rounded-lg px-2 py-2">
                <div class="order-1 sm:ml-6 xl:ml-0">
                    <h3 class="mb-1 text-gray-900 font-semibold dark:text-white">
                        <span class="mb-1 block text-xs leading-6 text-gray-500 dark:text-500 hover:text-gray-600 dark:hover:text-gray-400">2023-10-28</span>
                        <span>
                            Completely unstyled, fully accessible UI components
                        </span>
                    </h3>
                    <div class="font-sans text-gray-600 dark:text-gray-400">
                        <p>Completely unstyled, fully accessible UI components, designed to integrate beautifully with
                            Tailwind
                            CSS.
                        </p>
                    </div>
                    <!-- Actions -->
                    <div class="flex items-center space-x-1 my-6">
                        <!-- Beğeni -->
                        <button :to="(route.fullPath === '/') ? '/blog-post-1' : route.fullPath + '/blog-post-1'"
                            class="flex items-center font-sans font-semibold px-1 py-1 text-gray-600 dark:hover:text-gray-300 dark:text-gray-400 rounded-lg cursor-pointer hover:bg-gray-200 dark:hover:bg-gray-800">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                stroke="currentColor" class="w-5 h-5 mx-1 my-1">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z" />
                            </svg>
                            <!-- eger post begenilmisse gozukecek post begenilmemissse yukaridaki icon da gozukmeyecek -->
                            <!-- <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"
                            class="w-6 h-6 mx-1 my-1 text-red-600 dark:text-red-600">
                            <path
                                d="M11.645 20.91l-.007-.003-.022-.012a15.247 15.247 0 01-.383-.218 25.18 25.18 0 01-4.244-3.17C4.688 15.36 2.25 12.174 2.25 8.25 2.25 5.322 4.714 3 7.688 3A5.5 5.5 0 0112 5.052 5.5 5.5 0 0116.313 3c2.973 0 5.437 2.322 5.437 5.25 0 3.925-2.438 7.111-4.739 9.256a25.175 25.175 0 01-4.244 3.17 15.247 15.247 0 01-.383.219l-.022.012-.007.004-.003.001a.752.752 0 01-.704 0l-.003-.001z" />
                        </svg> -->
                            <span class="text-xs">1 {{ $t('like') }}</span>
                        </button>

                        <!-- Yorum -->
                        <button
                            class="flex items-center font-sans font-semibold px-1 py-1 text-gray-600 dark:hover:text-gray-300 dark:text-gray-400 rounded-lg cursor-pointer hover:bg-gray-200 dark:hover:bg-gray-800">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                stroke="currentColor" class="w-5 h-5 mx-1 my-1">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M12 20.25c4.97 0 9-3.694 9-8.25s-4.03-8.25-9-8.25S3 7.444 3 12c0 2.104.859 4.023 2.273 5.48.432.447.74 1.04.586 1.641a4.483 4.483 0 01-.923 1.785A5.969 5.969 0 006 21c1.282 0 2.47-.402 3.445-1.087.81.22 1.668.337 2.555.337z" />
                            </svg>
                            <span class="text-xs">6 {{ $t('comment') }}</span>
                        </button>

                        <!-- Kaydetme -->
                        <button
                            class="flex items-center font-sans font-semibold px-1 py-1 text-gray-600 dark:text-gray-400 rounded-lg cursor-pointer hover:bg-gray-200 hover:text-blue-600 dark:hover:bg-gray-800 dark:hover:text-blue-500">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                stroke="currentColor" class="w-5 h-5 mx-1 my-1">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M17.593 3.322c1.1.128 1.907 1.077 1.907 2.185V21L12 17.25 4.5 21V5.507c0-1.108.806-2.057 1.907-2.185a48.507 48.507 0 0111.186 0z" />
                            </svg>
                            <!-- post kaydedilirse ve zaten kayıt edilmisse gozukecek icon -->
                            <!-- <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"
                            class="w-6 h-6 mx-1 my-1 text-blue-600 dark:text-blue-600">
                            <path fill-rule="evenodd"
                                d="M6.32 2.577a49.255 49.255 0 0111.36 0c1.497.174 2.57 1.46 2.57 2.93V21a.75.75 0 01-1.085.67L12 18.089l-7.165 3.583A.75.75 0 013.75 21V5.507c0-1.47 1.073-2.756 2.57-2.93z"
                                clip-rule="evenodd" />
                        </svg> -->
                            <!-- Duruma gore save yazisi gozukebilir veya gozukmeyebilir -->
                            <!-- <span>{{ $t('save') }}</span> -->
                        </button>
                        <!-- Reading Time -->
                        <span
                            class="flex items-center text-xs font-sans font-semibold px-1 py-1 text-gray-600 dark:text-gray-400">
                            3 {{ $t('min-read') }}
                        </span>
                    </div>
                    <!-- Actions -->

                </div>
                <img src="https://via.placeholder.com/400x300" alt=""
                    class="mb-6 rounded-lg bg-slate-50 w-full sm:w-[17rem] sm:mb-0 xl:mb-6 xl:w-full" width="1216"
                    height="640">
            </RouterLink>
            <RouterLink :to="(route.fullPath === '/') ? '/blog-post-2' : route.fullPath + '/blog-post-2'"
                class="relative flex flex-col sm:flex-row xl:flex-col items-start border border-gray-300 dark:border-gray-700 hover:border-gray-400 dark:hover:border-gray-500 rounded-lg px-2 py-2">
                <div class="order-1 sm:ml-6 xl:ml-0">
                    <h3 class="mb-1 text-gray-900 font-semibold dark:text-white">
                        <span class="mb-1 block text-xs leading-6 text-gray-500 dark:text-500 hover:text-gray-600 dark:hover:text-gray-400">2023-10-28</span>
                        <span>
                            Completely unstyled, fully accessible UI components
                        </span>
                    </h3>
                    <div class="prose prose-slate prose-sm font-sans text-gray-600 dark:text-gray-400 dark:prose-dark">
                        <p>Completely unstyled, fully accessible UI components, designed to integrate beautifully with
                            Tailwind
                            CSS.
                        </p>
                    </div>
                    <!-- Actions -->
                    <div class="flex items-center space-x-1 my-6">
                        <!-- Beğeni -->
                        <button :to="(route.fullPath === '/') ? '/blog-post-1' : route.fullPath + '/blog-post-1'"
                            class="flex items-center font-sans font-semibold px-1 py-1 text-gray-600 dark:hover:text-gray-300 dark:text-gray-400 rounded-lg cursor-pointer hover:bg-gray-200 dark:hover:bg-gray-800">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                stroke="currentColor" class="w-5 h-5 mx-1 my-1">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z" />
                            </svg>
                            <!-- eger post begenilmisse gozukecek post begenilmemissse yukaridaki icon da gozukmeyecek -->
                            <!-- <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"
                            class="w-6 h-6 mx-1 my-1 text-red-600 dark:text-red-600">
                            <path
                                d="M11.645 20.91l-.007-.003-.022-.012a15.247 15.247 0 01-.383-.218 25.18 25.18 0 01-4.244-3.17C4.688 15.36 2.25 12.174 2.25 8.25 2.25 5.322 4.714 3 7.688 3A5.5 5.5 0 0112 5.052 5.5 5.5 0 0116.313 3c2.973 0 5.437 2.322 5.437 5.25 0 3.925-2.438 7.111-4.739 9.256a25.175 25.175 0 01-4.244 3.17 15.247 15.247 0 01-.383.219l-.022.012-.007.004-.003.001a.752.752 0 01-.704 0l-.003-.001z" />
                        </svg> -->
                            <span class="text-xs">1 {{ $t('like') }}</span>
                        </button>

                        <!-- Yorum -->
                        <button
                            class="flex items-center font-sans font-semibold px-1 py-1 text-gray-600 dark:hover:text-gray-300 dark:text-gray-400 rounded-lg cursor-pointer hover:bg-gray-200 dark:hover:bg-gray-800">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                stroke="currentColor" class="w-5 h-5 mx-1 my-1">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M12 20.25c4.97 0 9-3.694 9-8.25s-4.03-8.25-9-8.25S3 7.444 3 12c0 2.104.859 4.023 2.273 5.48.432.447.74 1.04.586 1.641a4.483 4.483 0 01-.923 1.785A5.969 5.969 0 006 21c1.282 0 2.47-.402 3.445-1.087.81.22 1.668.337 2.555.337z" />
                            </svg>
                            <span class="text-xs">6 {{ $t('comment') }}</span>
                        </button>

                        <!-- Kaydetme -->
                        <button
                            class="flex items-center font-sans font-semibold px-1 py-1 text-gray-600 dark:text-gray-400 rounded-lg cursor-pointer hover:bg-gray-200 hover:text-blue-600 dark:hover:bg-gray-800 dark:hover:text-blue-500">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                stroke="currentColor" class="w-5 h-5 mx-1 my-1">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M17.593 3.322c1.1.128 1.907 1.077 1.907 2.185V21L12 17.25 4.5 21V5.507c0-1.108.806-2.057 1.907-2.185a48.507 48.507 0 0111.186 0z" />
                            </svg>
                            <!-- post kaydedilirse ve zaten kayıt edilmisse gozukecek icon -->
                            <!-- <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"
                            class="w-6 h-6 mx-1 my-1 text-blue-600 dark:text-blue-600">
                            <path fill-rule="evenodd"
                                d="M6.32 2.577a49.255 49.255 0 0111.36 0c1.497.174 2.57 1.46 2.57 2.93V21a.75.75 0 01-1.085.67L12 18.089l-7.165 3.583A.75.75 0 013.75 21V5.507c0-1.47 1.073-2.756 2.57-2.93z"
                                clip-rule="evenodd" />
                        </svg> -->
                            <!-- Duruma gore save yazisi gozukebilir veya gozukmeyebilir -->
                            <!-- <span>{{ $t('save') }}</span> -->
                        </button>
                        <!-- Reading Time -->
                        <span
                            class="flex items-center text-xs font-sans font-semibold px-1 py-1 text-gray-600 dark:text-gray-400">
                            3 {{ $t('min-read') }}
                        </span>
                    </div>
                    <!-- Actions -->

                </div>
                <img src="https://via.placeholder.com/400x300" alt=""
                    class="mb-6 rounded-lg bg-slate-50 w-full sm:w-[17rem] sm:mb-0 xl:mb-6 xl:w-full" width="1216"
                    height="640">
            </RouterLink>
            <RouterLink :to="(route.fullPath === '/') ? '/blog-post-3' : route.fullPath + '/blog-post-3'"
                class="relative flex flex-col sm:flex-row xl:flex-col items-start border border-gray-300 dark:border-gray-700 hover:border-gray-400 dark:hover:border-gray-500 rounded-lg px-2 py-2">
                <div class="order-1 sm:ml-6 xl:ml-0">
                    <h3 class="mb-1 text-gray-900 font-semibold dark:text-white">
                        <span class="mb-1 block text-xs leading-6 text-gray-500 dark:text-500 hover:text-gray-600 dark:hover:text-gray-400">2023-10-28</span>
                        <span>
                            Completely unstyled, fully accessible UI components
                        </span>
                    </h3>
                    <div class="prose prose-slate prose-sm font-sans text-gray-600 dark:text-gray-400 dark:prose-dark">
                        <p>Completely unstyled, fully accessible UI components, designed to integrate beautifully with
                            Tailwind
                            CSS.
                        </p>
                    </div>
                    <!-- Actions -->
                    <div class="flex items-center space-x-1 my-6">
                        <!-- Beğeni -->
                        <button :to="(route.fullPath === '/') ? '/blog-post-1' : route.fullPath + '/blog-post-1'"
                            class="flex items-center font-sans font-semibold px-1 py-1 text-gray-600 dark:hover:text-gray-300 dark:text-gray-400 rounded-lg cursor-pointer hover:bg-gray-200 dark:hover:bg-gray-800">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                stroke="currentColor" class="w-5 h-5 mx-1 my-1">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z" />
                            </svg>
                            <!-- eger post begenilmisse gozukecek post begenilmemissse yukaridaki icon da gozukmeyecek -->
                            <!-- <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"
                            class="w-6 h-6 mx-1 my-1 text-red-600 dark:text-red-600">
                            <path
                                d="M11.645 20.91l-.007-.003-.022-.012a15.247 15.247 0 01-.383-.218 25.18 25.18 0 01-4.244-3.17C4.688 15.36 2.25 12.174 2.25 8.25 2.25 5.322 4.714 3 7.688 3A5.5 5.5 0 0112 5.052 5.5 5.5 0 0116.313 3c2.973 0 5.437 2.322 5.437 5.25 0 3.925-2.438 7.111-4.739 9.256a25.175 25.175 0 01-4.244 3.17 15.247 15.247 0 01-.383.219l-.022.012-.007.004-.003.001a.752.752 0 01-.704 0l-.003-.001z" />
                        </svg> -->
                            <span class="text-xs">1 {{ $t('like') }}</span>
                        </button>

                        <!-- Yorum -->
                        <button
                            class="flex items-center font-sans font-semibold px-1 py-1 text-gray-600 dark:hover:text-gray-300 dark:text-gray-400 rounded-lg cursor-pointer hover:bg-gray-200 dark:hover:bg-gray-800">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                stroke="currentColor" class="w-5 h-5 mx-1 my-1">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M12 20.25c4.97 0 9-3.694 9-8.25s-4.03-8.25-9-8.25S3 7.444 3 12c0 2.104.859 4.023 2.273 5.48.432.447.74 1.04.586 1.641a4.483 4.483 0 01-.923 1.785A5.969 5.969 0 006 21c1.282 0 2.47-.402 3.445-1.087.81.22 1.668.337 2.555.337z" />
                            </svg>
                            <span class="text-xs">6 {{ $t('comment') }}</span>
                        </button>

                        <!-- Kaydetme -->
                        <button
                            class="flex items-center font-sans font-semibold px-1 py-1 text-gray-600 dark:text-gray-400 rounded-lg cursor-pointer hover:bg-gray-200 hover:text-blue-600 dark:hover:bg-gray-800 dark:hover:text-blue-500">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                stroke="currentColor" class="w-5 h-5 mx-1 my-1">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M17.593 3.322c1.1.128 1.907 1.077 1.907 2.185V21L12 17.25 4.5 21V5.507c0-1.108.806-2.057 1.907-2.185a48.507 48.507 0 0111.186 0z" />
                            </svg>
                            <!-- post kaydedilirse ve zaten kayıt edilmisse gozukecek icon -->
                            <!-- <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"
                            class="w-6 h-6 mx-1 my-1 text-blue-600 dark:text-blue-600">
                            <path fill-rule="evenodd"
                                d="M6.32 2.577a49.255 49.255 0 0111.36 0c1.497.174 2.57 1.46 2.57 2.93V21a.75.75 0 01-1.085.67L12 18.089l-7.165 3.583A.75.75 0 013.75 21V5.507c0-1.47 1.073-2.756 2.57-2.93z"
                                clip-rule="evenodd" />
                        </svg> -->
                            <!-- Duruma gore save yazisi gozukebilir veya gozukmeyebilir -->
                            <!-- <span>{{ $t('save') }}</span> -->
                        </button>
                        <!-- Reading Time -->
                        <span
                            class="flex items-center text-xs font-sans font-semibold px-1 py-1 text-gray-600 dark:text-gray-400">
                            3 {{ $t('min-read') }}
                        </span>
                    </div>
                    <!-- Actions -->

                </div>
                <img src="https://via.placeholder.com/400x300" alt=""
                    class="mb-6 rounded-lg bg-slate-50 w-full sm:w-[17rem] sm:mb-0 xl:mb-6 xl:w-full" width="1216"
                    height="640">
            </RouterLink>
        </ul>
    </section>
</template>

<style lang="scss" scoped></style>