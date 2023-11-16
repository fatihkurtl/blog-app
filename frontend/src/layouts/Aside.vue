<script setup>

</script>

<template>
    <aside class="col-span-1 hidden md:hidden lg:block">
        <div class="bg-lightItemsColor dark:bg-darkItemsColor p-4">
            <!-- SEARCH BAR-->
            <div class="flex md:order-2 justify-end">
                <button type="button" data-collapse-toggle="navbar-search" aria-controls="navbar-search"
                    aria-expanded="false"
                    class="md:hidden hidden text-gray-500 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700 focus:outline-none focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-700 rounded-lg text-sm p-2.5 mr-1">
                    <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
                        viewBox="0 0 20 20">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z" />
                    </svg>
                    <span class="sr-only">Search</span>
                </button>
                <div class="relative hidden md:block min-w-full">
                    <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
                        <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true"
                            xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z" />
                        </svg>
                        <span class="sr-only">Search icon</span>
                    </div>
                    <input type="text" id="search-navbar"
                        class="block w-full p-2 pl-10 font-sans font-semibold text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-black dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                        :placeholder="$t('search')">
                </div>
            </div>
            <!-- SEARCH BAR -->
        </div>
        <div class="bg-lightItemsColor dark:bg-darkItemsColor p-2 my-2">
            <h3 class="text-xl font-sans font-bold text-gray-600 dark:text-white mb-4 mx-2 my-2">{{ $t('latest-posts') }}</h3>
            <ul>
                <li class="py-3 px-3 dark:hover:bg-neutral-800 hover:bg-neutral-200 rounded-lg sm:py-4 mb-2">
                    <RouterLink to="/post-detail-1" class="flex items-center">
                        <div class="flex-shrink-0">
                            <img class="w-8 h-8 rounded-full" src="https://via.placeholder.com/400x300" alt="Neil image">
                        </div>
                        <div class="flex-1 min-w-0 ms-4">
                            <p class="text-md font-sans font-semibold text-gray-600 truncate dark:text-white">
                                Blog Post 1
                            </p>
                            <p class="text-sm text-gray-500 truncate dark:text-gray-400">
                                Lorem ipsum dolor sit amet, consectetur adipiscing
                                elit. Vivamus quis porta dui. Ut eu iaculis massa.
                            </p>
                        </div>
                    </RouterLink>
                </li>
                <li class="py-3 px-3 dark:hover:bg-neutral-800 hover:bg-neutral-200 rounded-lg sm:py-4 mb-2">
                    <RouterLink to="/post-detail-2" class="flex items-center">
                        <div class="flex-shrink-0">
                            <img class="w-8 h-8 rounded-full" src="https://via.placeholder.com/400x300" alt="Neil image">
                        </div>
                        <div class="flex-1 min-w-0 ms-4">
                            <p class="text-md font-sans font-semibold text-gray-600 truncate dark:text-white">
                                Blog Post 2
                            </p>
                            <p class="text-sm text-gray-500 truncate dark:text-gray-400">
                                Lorem ipsum dolor sit amet, consectetur adipiscing
                                elit. Vivamus quis porta dui. Ut eu iaculis massa.
                            </p>
                        </div>
                    </RouterLink>
                </li>
                <li class="py-3 px-3 dark:hover:bg-neutral-800 hover:bg-neutral-200 rounded-lg sm:py-4 mb-2">
                    <RouterLink to="/post-detail-3" class="flex items-center">
                        <div class="flex-shrink-0">
                            <img class="w-8 h-8 rounded-full" src="https://via.placeholder.com/400x300" alt="Neil image">
                        </div>
                        <div class="flex-1 min-w-0 ms-4">
                            <p class="text-md font-sans font-semibold text-gray-600 truncate dark:text-white">
                                Blog Post 3
                            </p>
                            <p class="text-sm text-gray-500 truncate dark:text-gray-400">
                                Lorem ipsum dolor sit amet, consectetur adipiscing
                                elit. Vivamus quis porta dui. Ut eu iaculis massa.
                            </p>
                        </div>
                    </RouterLink>
                </li>
                <!-- Daha fazla post eklemek için liste öğelerini çoğaltabilirsiniz -->
            </ul>
            <hr class="w-full h-1 my-8 bg-gray-200 border-0 dark:bg-darkBgColor">
            <h3 class="text-xl font-sans font-bold text-gray-600 dark:text-white mb-4 mx-2 my-2">{{ $t('trends') }}</h3>
            <ul>
                <li class="py-3 px-3 dark:hover:bg-neutral-800 hover:bg-neutral-200 rounded-lg sm:py-4 mb-2">
                    <RouterLink to="/trends/post-detail-1" class="flex items-center">
                        <div class="flex-shrink-0">
                            <img class="w-8 h-8 rounded-full" src="https://via.placeholder.com/400x300" alt="Neil image">
                        </div>
                        <div class="flex-1 min-w-0 ms-4">
                            <p class="text-md font-sans font-semibold text-gray-600 truncate dark:text-white">
                                Blog Post 1
                            </p>
                            <p class="text-sm text-gray-500 truncate dark:text-gray-400">
                                Lorem ipsum dolor sit amet, consectetur adipiscing
                                elit. Vivamus quis porta dui. Ut eu iaculis massa.
                            </p>
                        </div>
                    </RouterLink>
                </li>
                <li class="py-3 px-3 dark:hover:bg-neutral-800 hover:bg-neutral-200 rounded-lg sm:py-4 mb-2">
                    <RouterLink to="/trends/post-detail-2" class="flex items-center">
                        <div class="flex-shrink-0">
                            <img class="w-8 h-8 rounded-full" src="https://via.placeholder.com/400x300" alt="Neil image">
                        </div>
                        <div class="flex-1 min-w-0 ms-4">
                            <p class="text-md font-sans font-semibold text-gray-600 truncate dark:text-white">
                                Blog Post 2
                            </p>
                            <p class="text-sm text-gray-500 truncate dark:text-gray-400">
                                Lorem ipsum dolor sit amet, consectetur adipiscing
                                elit. Vivamus quis porta dui. Ut eu iaculis massa.
                            </p>
                        </div>
                    </RouterLink>
                </li>
                <li class="py-3 px-3 dark:hover:bg-neutral-800 hover:bg-neutral-200 rounded-lg sm:py-4 mb-2">
                    <RouterLink to="/trends/post-detail-3" class="flex items-center dark:hover:text-gray-300">
                        <div class="flex-shrink-0">
                            <img class="w-8 h-8 rounded-full" src="https://via.placeholder.com/400x300" alt="Neil image">
                        </div>
                        <div class="flex-1 min-w-0 ms-4">
                            <p class="text-md font-sans font-semibold text-gray-600 truncate dark:text-white">
                                Blog Post 3
                            </p>
                            <p class="text-sm text-gray-500 truncate dark:text-gray-400">
                                Lorem ipsum dolor sit amet, consectetur adipiscing
                                elit. Vivamus quis porta dui. Ut eu iaculis massa.
                            </p>
                        </div>
                    </RouterLink>
                </li>
                <!-- Daha fazla post eklemek için liste öğelerini çoğaltabilirsiniz -->
            </ul>
            <!-- <hr class="w-full h-1 my-8 bg-gray-200 border-0 dark:bg-darkBgColor"> -->
        </div>
        <!-- Email Subscribe  -->
        <div class="py-2 lg:py-2 px-4 mx-auto max-w-screen-md bg-lightItemsColor dark:bg-darkItemsColor mb-4">
            <h4 class="text-2xl my-4 font-semibold text-center text-gray-600 dark:text-white">
                {{ $t('subscribe-newsletter') }}
            </h4>
            <form action="#" method="post" class="flex">
                <input type="email" name="email" :placeholder="$t('your-email')"
                    class="w-full p-2 m-2 mr-2 text-gray-600 text-sm font-sans font-semibold dark:text-white bg-gray-50 dark:bg-black border rounded-l focus:outline-none focus:border-blue-300">
                <button type="submit"
                    class="px-2 py-2 m-2 rounded-r font-sans font-semibold text-white bg-lightBtnColor hover:bg-sky-600 dark:hover:bg-sky-700 focus:ring-4 dark:bg-darkBtnColor dark:focus:ring-sky-800 focus:ring-blue-300">
                    {{ $t('subscribe-btn') }}
                </button>
            </form>
        </div>
        <!-- Email Subscribe  -->
    </aside>
</template>

<style lang="scss" scoped></style>
