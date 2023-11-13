<script setup>

</script>

<template>
    <section class="mx-auto my-4 p-8 bg-lightItemsColor dark:bg-darkItemsColor">
        <!-- Örnek Kaydedilmiş Postlar -->
        <div
            class="w-full mx-auto max-w-5xl p-4 border border-gray-200 dark:border-gray-700 bg-lightItemsColor rounded-lg sm:p-8 dark:bg-darkItemsColor">
            <div class="flex items-center justify-between mb-4">
                <h2 class="text-2xl font-bold text-gray-600 dark:text-white mb-4">{{ $t('reading-list') }} (0)</h2>                
            </div>
            <div class="flow-root">
                <ul role="list" class="divide-y divide-gray-200 dark:divide-gray-700">
                    <li class="py-3 sm:py-4">
                        <div class="flex items-center">
                            <div class="flex-shrink-0">
                                <img class="w-8 h-8 rounded-full" src="https://via.placeholder.com/400x300"
                                    alt="Neil image">
                            </div>
                            <div class="flex-1 min-w-0 ms-4">
                                <p class="text-sm font-sans font-semibold text-gray-600 truncate dark:text-white">
                                    Blog Post 1
                                </p>
                                <p class="text-sm text-gray-500 truncate dark:text-gray-400">
                                    Lorem ipsum dolor sit amet, consectetur adipiscing
                                    elit. Vivamus quis porta dui. Ut eu iaculis massa.
                                </p>
                            </div>
                            <div class="inline-flex items-center text-base font-semibold text-gray-900 dark:text-white">
                                <!-- Kaydetme -->
                                <button
                                    class="flex items-center font-sans font-semibold px-1 py-1 text-gray-600 dark:text-gray-400 rounded-lg cursor-pointer hover:bg-gray-200 hover:text-blue-600 dark:hover:bg-gray-800 dark:hover:text-blue-500">
                                    <!-- Tiklandiginda bu icon aktif olacak -->
                                    <!-- <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                                        stroke-width="1.5" stroke="currentColor" class="w-6 h-6 mx-1 my-1">
                                        <path stroke-linecap="round" stroke-linejoin="round"
                                            d="M17.593 3.322c1.1.128 1.907 1.077 1.907 2.185V21L12 17.25 4.5 21V5.507c0-1.108.806-2.057 1.907-2.185a48.507 48.507 0 0111.186 0z" />
                                    </svg> -->
                                    <!-- Post kayitli olacagi icin bu icon gozukecek degilse yukaridaki -->
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"
                                        class="w-6 h-6 mx-1 my-1">
                                        <path fill-rule="evenodd"
                                            d="M6.32 2.577a49.255 49.255 0 0111.36 0c1.497.174 2.57 1.46 2.57 2.93V21a.75.75 0 01-1.085.67L12 18.089l-7.165 3.583A.75.75 0 013.75 21V5.507c0-1.47 1.073-2.756 2.57-2.93z"
                                            clip-rule="evenodd" />
                                    </svg>

                                </button>
                                <!-- Kaydetme -->

                            </div>
                        </div>
                    </li>
                    <li class="py-3 sm:py-4">
                        <div class="flex items-center ">
                            <div class="flex-shrink-0">
                                <img class="w-8 h-8 rounded-full" src="https://via.placeholder.com/400x300"
                                    alt="Bonnie image">
                            </div>
                            <div class="flex-1 min-w-0 ms-4">
                                <p class="text-sm font-sans font-semibold text-gray-600 truncate dark:text-white">
                                    Blog Post 2
                                </p>
                                <p class="text-sm text-gray-500 truncate dark:text-gray-400">
                                    Lorem ipsum dolor sit amet, consectetur adipiscing
                                    elit. Vivamus quis porta dui. Ut eu iaculis massa.
                                </p>
                            </div>
                            <div class="inline-flex items-center text-base font-semibold text-gray-900 dark:text-white">
                                <!-- Kaydetme -->
                                <button
                                    class="flex items-center font-sans font-semibold px-1 py-1 text-gray-600 dark:text-gray-400 rounded-lg cursor-pointer hover:bg-gray-200 hover:text-blue-600 dark:hover:bg-gray-800 dark:hover:text-blue-500">
                                    <!-- <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                                        stroke-width="1.5" stroke="currentColor" class="w-6 h-6 mx-1 my-1">
                                        <path stroke-linecap="round" stroke-linejoin="round"
                                            d="M17.593 3.322c1.1.128 1.907 1.077 1.907 2.185V21L12 17.25 4.5 21V5.507c0-1.108.806-2.057 1.907-2.185a48.507 48.507 0 0111.186 0z" />
                                    </svg> -->
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"
                                        class="w-6 h-6 mx-1 my-1">
                                        <path fill-rule="evenodd"
                                            d="M6.32 2.577a49.255 49.255 0 0111.36 0c1.497.174 2.57 1.46 2.57 2.93V21a.75.75 0 01-1.085.67L12 18.089l-7.165 3.583A.75.75 0 013.75 21V5.507c0-1.47 1.073-2.756 2.57-2.93z"
                                            clip-rule="evenodd" />
                                    </svg>
                                </button>
                                <!-- Kaydetme -->
                            </div>
                        </div>
                    </li>
                    <li class="py-3 sm:py-4">
                        <div class="flex items-center">
                            <div class="flex-shrink-0">
                                <img class="w-8 h-8 rounded-full" src="https://via.placeholder.com/400x300"
                                    alt="Michael image">
                            </div>
                            <div class="flex-1 min-w-0 ms-4">
                                <p class="text-sm font-sans font-semibold text-gray-600 truncate dark:text-white">
                                    Blog Post 3
                                </p>
                                <p class="text-sm text-gray-500 truncate dark:text-gray-400">
                                    Lorem ipsum dolor sit amet, consectetur adipiscing
                                    elit. Vivamus quis porta dui. Ut eu iaculis massa.
                                </p>
                            </div>
                            <div class="inline-flex items-center text-base font-semibold text-gray-900 dark:text-white">
                                <!-- Kaydetme -->
                                <button
                                    class="flex items-center font-sans font-semibold px-1 py-1 text-gray-600 dark:text-gray-400 rounded-lg cursor-pointer hover:bg-gray-200 hover:text-blue-600 dark:hover:bg-gray-800 dark:hover:text-blue-500">
                                    <!-- <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                                        stroke-width="1.5" stroke="currentColor" class="w-6 h-6 mx-1 my-1">
                                        <path stroke-linecap="round" stroke-linejoin="round"
                                            d="M17.593 3.322c1.1.128 1.907 1.077 1.907 2.185V21L12 17.25 4.5 21V5.507c0-1.108.806-2.057 1.907-2.185a48.507 48.507 0 0111.186 0z" />
                                    </svg> -->
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"
                                        class="w-6 h-6 mx-1 my-1">
                                        <path fill-rule="evenodd"
                                            d="M6.32 2.577a49.255 49.255 0 0111.36 0c1.497.174 2.57 1.46 2.57 2.93V21a.75.75 0 01-1.085.67L12 18.089l-7.165 3.583A.75.75 0 013.75 21V5.507c0-1.47 1.073-2.756 2.57-2.93z"
                                            clip-rule="evenodd" />
                                    </svg>
                                </button>
                                <!-- Kaydetme -->
                            </div>
                        </div>
                    </li>
                    <li class="py-3 sm:py-4">
                        <div class="flex items-center ">
                            <div class="flex-shrink-0">
                                <img class="w-8 h-8 rounded-full" src="https://via.placeholder.com/400x300"
                                    alt="Lana image">
                            </div>
                            <div class="flex-1 min-w-0 ms-4">
                                <p class="text-sm font-sans font-semibold text-gray-600 truncate dark:text-white">
                                    Blog Post 4
                                </p>
                                <p class="text-sm text-gray-500 truncate dark:text-gray-400">
                                    Lorem ipsum dolor sit amet, consectetur adipiscing
                                    elit. Vivamus quis porta dui. Ut eu iaculis massa.
                                </p>
                            </div>
                            <div class="inline-flex items-center text-base font-semibold text-gray-900 dark:text-white">
                                <!-- Kaydetme -->
                                <button
                                    class="flex items-center font-sans font-semibold px-1 py-1 text-gray-600 dark:text-gray-400 rounded-lg cursor-pointer hover:bg-gray-200 hover:text-blue-600 dark:hover:bg-gray-800 dark:hover:text-blue-500">
                                    <!-- <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                                        stroke-width="1.5" stroke="currentColor" class="w-6 h-6 mx-1 my-1">
                                        <path stroke-linecap="round" stroke-linejoin="round"
                                            d="M17.593 3.322c1.1.128 1.907 1.077 1.907 2.185V21L12 17.25 4.5 21V5.507c0-1.108.806-2.057 1.907-2.185a48.507 48.507 0 0111.186 0z" />
                                    </svg> -->
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"
                                        class="w-6 h-6 mx-1 my-1">
                                        <path fill-rule="evenodd"
                                            d="M6.32 2.577a49.255 49.255 0 0111.36 0c1.497.174 2.57 1.46 2.57 2.93V21a.75.75 0 01-1.085.67L12 18.089l-7.165 3.583A.75.75 0 013.75 21V5.507c0-1.47 1.073-2.756 2.57-2.93z"
                                            clip-rule="evenodd" />
                                    </svg>
                                </button>
                                <!-- Kaydetme -->
                            </div>
                        </div>
                    </li>
                    <li class="pt-3 pb-0 sm:pt-4">
                        <div class="flex items-center ">
                            <div class="flex-shrink-0">
                                <img class="w-8 h-8 rounded-full" src="https://via.placeholder.com/400x300"
                                    alt="Thomas image">
                            </div>
                            <div class="flex-1 min-w-0 ms-4">
                                <p class="text-sm font-sans font-semibold text-gray-600 truncate dark:text-white">
                                    Blog Post 5
                                </p>
                                <p class="text-sm text-gray-500 truncate dark:text-gray-400">
                                    Lorem ipsum dolor sit amet, consectetur adipiscing
                                    elit. Vivamus quis porta dui. Ut eu iaculis massa.
                                </p>
                            </div>
                            <div class="inline-flex items-center text-base font-semibold text-gray-900 dark:text-white">
                                <!-- Kaydetme -->
                                <button
                                    class="flex items-center font-sans font-semibold px-1 py-1 text-gray-600 dark:text-gray-400 rounded-lg cursor-pointer hover:bg-gray-200 hover:text-blue-600 dark:hover:bg-gray-800 dark:hover:text-blue-500">
                                    <!-- <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                                        stroke-width="1.5" stroke="currentColor" class="w-6 h-6 mx-1 my-1">
                                        <path stroke-linecap="round" stroke-linejoin="round"
                                            d="M17.593 3.322c1.1.128 1.907 1.077 1.907 2.185V21L12 17.25 4.5 21V5.507c0-1.108.806-2.057 1.907-2.185a48.507 48.507 0 0111.186 0z" />
                                    </svg> -->
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"
                                        class="w-6 h-6 mx-1 my-1">
                                        <path fill-rule="evenodd"
                                            d="M6.32 2.577a49.255 49.255 0 0111.36 0c1.497.174 2.57 1.46 2.57 2.93V21a.75.75 0 01-1.085.67L12 18.089l-7.165 3.583A.75.75 0 013.75 21V5.507c0-1.47 1.073-2.756 2.57-2.93z"
                                            clip-rule="evenodd" />
                                    </svg>
                                </button>
                                <!-- Kaydetme -->
                            </div>
                        </div>
                    </li>
                </ul>
            </div>
        </div>

    </section>
</template>

<style  scoped></style>