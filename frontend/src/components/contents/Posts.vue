<script setup>
import { useRoute, useRouter } from 'vue-router';


const route = useRoute();

</script>

<template>
    <div class="col-span-2">
        <!-- Blog Post 1 -->
        <RouterLink :to="(route.fullPath === '/') ? '/blog-post-1' : route.fullPath + '/blog-post-1'"
            class="bg-lightItemsColor dark:bg-darkItemsColor overflow-hidden mb-6 flex flex-col md:flex-row">
            <img src="https://via.placeholder.com/400x300" alt="Blog Post Image"
                class="w-full md:w-1/3 h-auto object-cover">
            <div class="w-full md:w-2/3 p-4">
                <div class="px-1 py-1">
                    <h2 class="text-2xl md:text-3xl lg:text-3xl font-sans font-bold text-gray-600 dark:text-white mb-2">
                        Blog Post Title 1
                    </h2>
                    <p class="text-gray-800 font-sans dark:text-gray-300 mb-2 my-4 lg:my-8">
                        Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit. Vivamus quis porta dui. Ut eu iaculis massa.
                    </p>
                    <!-- <RouterLink :to="(route.fullPath === '/') ? '/blog-post-1' : route.fullPath + '/blog-post-1'"
                    class="text-blue-500 hover:underline">{{ $t('read-more') }}</RouterLink> -->
                    <span class="text-xs font-sans text-gray-600 dark:text-gray-400">2023-10-28</span>
                </div>
                <!-- Actions -->
                <div class="flex items-center space-x-4 my-6">
                    <!-- Beğeni -->
                    <button
                        class="flex items-center font-sans font-semibold px-1 py-1 text-gray-600 dark:hover:text-gray-300 dark:text-gray-400 rounded-lg cursor-pointer hover:bg-gray-200 dark:hover:bg-gray-800">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                            stroke="currentColor" class="w-6 h-6 mx-1 my-1">
                            <path stroke-linecap="round" stroke-linejoin="round"
                                d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z" />
                        </svg>
                        <!-- eger post begenilmisse gozukecek post begenilmemissse yukaridaki icon da gozukmeyecek -->
                        <!-- <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"
                            class="w-6 h-6 mx-1 my-1 text-red-600 dark:text-red-600">
                            <path
                                d="M11.645 20.91l-.007-.003-.022-.012a15.247 15.247 0 01-.383-.218 25.18 25.18 0 01-4.244-3.17C4.688 15.36 2.25 12.174 2.25 8.25 2.25 5.322 4.714 3 7.688 3A5.5 5.5 0 0112 5.052 5.5 5.5 0 0116.313 3c2.973 0 5.437 2.322 5.437 5.25 0 3.925-2.438 7.111-4.739 9.256a25.175 25.175 0 01-4.244 3.17 15.247 15.247 0 01-.383.219l-.022.012-.007.004-.003.001a.752.752 0 01-.704 0l-.003-.001z" />
                        </svg> -->
                        <span>1 {{ $t('like') }}</span>
                    </button>

                    <!-- Yorum -->
                    <button
                        class="flex items-center font-sans font-semibold px-1 py-1 text-gray-600 dark:hover:text-gray-300 dark:text-gray-400 rounded-lg cursor-pointer hover:bg-gray-200 dark:hover:bg-gray-800">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                            stroke="currentColor" class="w-6 h-6 mx-1 my-1">
                            <path stroke-linecap="round" stroke-linejoin="round"
                                d="M12 20.25c4.97 0 9-3.694 9-8.25s-4.03-8.25-9-8.25S3 7.444 3 12c0 2.104.859 4.023 2.273 5.48.432.447.74 1.04.586 1.641a4.483 4.483 0 01-.923 1.785A5.969 5.969 0 006 21c1.282 0 2.47-.402 3.445-1.087.81.22 1.668.337 2.555.337z" />
                        </svg>
                        <span>6 {{ $t('comment') }}</span>
                    </button>

                    <!-- Kaydetme -->
                    <button
                        class="flex items-center font-sans font-semibold px-1 py-1 text-gray-600 dark:text-gray-400 rounded-lg cursor-pointer hover:bg-gray-200 hover:text-blue-600 dark:hover:bg-gray-800 dark:hover:text-blue-500">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                            stroke="currentColor" class="w-6 h-6 mx-1 my-1">
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
                </div>
                <!-- Actions -->
                <!-- Reading Time -->
                <div class="flex justify-end space-x-4">
                    <div class="flex items-center text-xs font-sans text-gray-600 dark:text-gray-400">
                        <!-- <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                            stroke="currentColor" class="w-5 h-5 mx-1 my-1">
                            <path stroke-linecap="round" stroke-linejoin="round"
                                d="M2.036 12.322a1.012 1.012 0 010-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.963-7.178z" />
                            <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                        </svg> -->
                        <span class="lg:mt-8">3 {{ $t('min-read') }}</span>

                    </div>
                </div>
                <!-- Reading Time -->
            </div>
        </RouterLink>

        <!-- Blog Post 2 -->
        <RouterLink :to="(route.fullPath === '/') ? '/blog-post-2' : route.fullPath + '/blog-post-2'"
            class="bg-lightItemsColor dark:bg-darkItemsColor overflow-hidden mb-6 flex flex-col md:flex-row">
            <img src="https://via.placeholder.com/400x300" alt="Blog Post Image"
                class="w-full md:w-1/3 h-auto object-cover">
            <div class="w-full md:w-2/3 p-4">
                <div class="px-1 py-1">
                    <h2 class="text-2xl md:text-3xl lg:text-3xl font-sans font-bold text-gray-600 dark:text-white mb-2">
                        Blog Post Title 2
                    </h2>
                    <p class="text-gray-800 font-sans dark:text-gray-300 my-4 lg:my-8">
                        Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit. Vivamus quis porta dui. Ut eu iaculis massa.
                    </p>
                    <!-- <RouterLink :to="(route.fullPath === '/') ? '/blog-post-2' : route.fullPath + '/blog-post-2'"
                    class="text-blue-500 hover:underline">
                    {{ $t('read-more') }}
                </RouterLink> -->
                    <span class="text-xs font-sans text-gray-600 dark:text-gray-400">2023-10-28</span>
                </div>
                <!-- Actions -->
                <div class="flex items-center space-x-4 my-6">
                    <!-- Beğeni -->
                    <button
                        class="flex items-center font-sans font-semibold px-1 py-1 text-gray-600 dark:hover:text-gray-300 dark:text-gray-400 rounded-lg cursor-pointer hover:bg-gray-200 dark:hover:bg-gray-800">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                            stroke="currentColor" class="w-6 h-6 mx-1 my-1">
                            <path stroke-linecap="round" stroke-linejoin="round"
                                d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z" />
                        </svg>
                        <!-- eger post begenilmisse gozukecek post begenilmemissse yukaridaki icon da gozukmeyecek -->
                        <!-- <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"
                            class="w-6 h-6 mx-1 my-1 text-red-600 dark:text-red-600">
                            <path
                                d="M11.645 20.91l-.007-.003-.022-.012a15.247 15.247 0 01-.383-.218 25.18 25.18 0 01-4.244-3.17C4.688 15.36 2.25 12.174 2.25 8.25 2.25 5.322 4.714 3 7.688 3A5.5 5.5 0 0112 5.052 5.5 5.5 0 0116.313 3c2.973 0 5.437 2.322 5.437 5.25 0 3.925-2.438 7.111-4.739 9.256a25.175 25.175 0 01-4.244 3.17 15.247 15.247 0 01-.383.219l-.022.012-.007.004-.003.001a.752.752 0 01-.704 0l-.003-.001z" />
                        </svg> -->
                        <span>1 {{ $t('like') }}</span>
                    </button>

                    <!-- Yorum -->
                    <button
                        class="flex items-center font-sans font-semibold px-1 py-1 text-gray-600 dark:hover:text-gray-300 dark:text-gray-400 rounded-lg cursor-pointer hover:bg-gray-200 dark:hover:bg-gray-800">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                            stroke="currentColor" class="w-6 h-6 mx-1 my-1">
                            <path stroke-linecap="round" stroke-linejoin="round"
                                d="M12 20.25c4.97 0 9-3.694 9-8.25s-4.03-8.25-9-8.25S3 7.444 3 12c0 2.104.859 4.023 2.273 5.48.432.447.74 1.04.586 1.641a4.483 4.483 0 01-.923 1.785A5.969 5.969 0 006 21c1.282 0 2.47-.402 3.445-1.087.81.22 1.668.337 2.555.337z" />
                        </svg>
                        <span>6 {{ $t('comment') }}</span>
                    </button>

                    <!-- Kaydetme -->
                    <button
                        class="flex items-center font-sans font-semibold px-1 py-1 text-gray-600 dark:text-gray-400 rounded-lg cursor-pointer hover:bg-gray-200 hover:text-blue-600 dark:hover:bg-gray-800 dark:hover:text-blue-500">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                            stroke="currentColor" class="w-6 h-6 mx-1 my-1">
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
                </div>
                <!-- Actions -->
                <!-- Reading Time -->
                <div class="flex justify-end space-x-4">
                    <div class="flex items-center text-xs text-gray-600 dark:text-gray-400 font-sans">
                        <!-- <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                            stroke="currentColor" class="w-5 h-5 mr-1">
                            <path stroke-linecap="round" stroke-linejoin="round"
                                d="M2.036 12.322a1.012 1.012 0 010-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.963-7.178z" />
                            <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                        </svg> -->
                        <span class="lg:mt-8">3 {{ $t('min-read') }}</span>
                    </div>
                </div>
                <!-- Reading Time -->
            </div>
        </RouterLink>

        <!-- Blog Post 3 -->
        <RouterLink :to="(route.fullPath === '/') ? '/blog-post-3' : route.fullPath + '/blog-post-3'"
            class="bg-lightItemsColor dark:bg-darkItemsColor overflow-hidden mb-6 flex flex-col md:flex-row">
            <img src="https://via.placeholder.com/400x300" alt="Blog Post Image"
                class="w-full md:w-1/3 h-auto object-cover">
            <div class="w-full md:w-2/3 p-4">
                <div class="px-1 py-1">
                    <h2 class="text-2xl md:text-3xl lg:text-3xl font-sans font-bold text-gray-600 dark:text-white mb-2">
                        Blog Post Title 3
                    </h2>
                    <p class="text-gray-800 font-sans dark:text-gray-300 my-4 lg:my-8">
                        Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit. Vivamus quis porta dui. Ut eu iaculis massa.
                    </p>
                    <!-- <RouterLink :to="(route.fullPath === '/') ? '/blog-post-3' : route.fullPath + '/blog-post-3'"
                    class="text-blue-500 hover:underline">
                    {{ $t('read-more') }}
                </RouterLink> -->
                    <span class="text-xs font-sans text-gray-600 dark:text-gray-400">2023-10-28</span>
                </div>
                <!-- Actions -->
                <div class="flex items-center space-x-4 my-6">
                    <!-- Beğeni -->
                    <button
                        class="flex items-center font-sans font-semibold px-1 py-1 text-gray-600 dark:hover:text-gray-300 dark:text-gray-400 rounded-lg cursor-pointer hover:bg-gray-200 dark:hover:bg-gray-800">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                            stroke="currentColor" class="w-6 h-6 mx-1 my-1">
                            <path stroke-linecap="round" stroke-linejoin="round"
                                d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z" />
                        </svg>
                        <!-- eger post begenilmisse gozukecek post begenilmemissse yukaridaki icon da gozukmeyecek -->
                        <!-- <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"
                            class="w-6 h-6 mx-1 my-1 text-red-600 dark:text-red-600">
                            <path
                                d="M11.645 20.91l-.007-.003-.022-.012a15.247 15.247 0 01-.383-.218 25.18 25.18 0 01-4.244-3.17C4.688 15.36 2.25 12.174 2.25 8.25 2.25 5.322 4.714 3 7.688 3A5.5 5.5 0 0112 5.052 5.5 5.5 0 0116.313 3c2.973 0 5.437 2.322 5.437 5.25 0 3.925-2.438 7.111-4.739 9.256a25.175 25.175 0 01-4.244 3.17 15.247 15.247 0 01-.383.219l-.022.012-.007.004-.003.001a.752.752 0 01-.704 0l-.003-.001z" />
                        </svg> -->
                        <span>1 {{ $t('like') }}</span>
                    </button>

                    <!-- Yorum -->
                    <button
                        class="flex items-center font-sans font-semibold px-1 py-1 text-gray-600 dark:hover:text-gray-300 dark:text-gray-400 rounded-lg cursor-pointer hover:bg-gray-200 dark:hover:bg-gray-800">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                            stroke="currentColor" class="w-6 h-6 mx-1 my-1">
                            <path stroke-linecap="round" stroke-linejoin="round"
                                d="M12 20.25c4.97 0 9-3.694 9-8.25s-4.03-8.25-9-8.25S3 7.444 3 12c0 2.104.859 4.023 2.273 5.48.432.447.74 1.04.586 1.641a4.483 4.483 0 01-.923 1.785A5.969 5.969 0 006 21c1.282 0 2.47-.402 3.445-1.087.81.22 1.668.337 2.555.337z" />
                        </svg>
                        <span>6 {{ $t('comment') }}</span>
                    </button>

                    <!-- Kaydetme -->
                    <button
                        class="flex items-center font-sans font-semibold px-1 py-1 text-gray-600 dark:text-gray-400 rounded-lg cursor-pointer hover:bg-gray-200 hover:text-blue-600 dark:hover:bg-gray-800 dark:hover:text-blue-500">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                            stroke="currentColor" class="w-6 h-6 mx-1 my-1">
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
                </div>
                <!-- Actions -->
                <!-- Reading Time -->
                <div class="flex justify-end space-x-4">
                    <div class="flex items-center text-xs text-gray-600 dark:text-gray-400 font-sans">
                        <!-- <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                            stroke="currentColor" class="w-5 h-5 mr-1">
                            <path stroke-linecap="round" stroke-linejoin="round"
                                d="M2.036 12.322a1.012 1.012 0 010-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.963-7.178z" />
                            <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                        </svg> -->
                        <span class="lg:mt-8">3 {{ $t('min-read') }}</span>
                    </div>
                </div>
                <!-- Reading Time -->
            </div>
        </RouterLink>
    </div>
</template>

<style lang="scss" scoped></style>