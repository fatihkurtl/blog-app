<script setup>
import { ref, onMounted } from 'vue';
import { RouterLink, useRouter, RouterView } from 'vue-router';
import { onClickOutside } from '@vueuse/core';
import { useThemeStore } from '../stores/theme';
import { useLangStore } from '../stores/language';

const theme = useThemeStore();
const language = useLangStore();

// onMounted(() => {
//     document.cookie = 'locale=EN'
// });


const isNavbarOpen = ref(false);
const toggleNavbar = () => {
    isNavbarOpen.value = !isNavbarOpen.value;
};

const userDropdown = ref(false);
const toggleUser = () => {
    userDropdown.value = !userDropdown.value;
}

onClickOutside(isNavbarOpen, (event) => {
    isNavbarOpen.value = false;
});

onClickOutside(userDropdown, (event) => {
    userDropdown.value = false;
});
</script>

<template>
    <!-- <nav>
        <RouterLink class="text-black dark:text-white" to="/">Home</RouterLink>
    </nav> -->

    <nav class="bg-lightItemsColor dark:border-borderColor dark:bg-darkItemsColor min-w-screen">
        <div class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
            <RouterLink to="/" class="flex items-center">
                <img src="../assets//logo.svg" class="h-8 mr-3" alt="Vue Logo" />
                <span class="self-center text-2xl font-bold whitespace-nowrap dark:text-white">./fullstack
                    <span class="text-sm font-semibold text-gray-400 dark:text-gray-500">v0.1.0</span>
                </span>
            </RouterLink>
            <!-- SEARCH BAR-->
            <div class="flex md:order-2">
                <button type="button" data-collapse-toggle="navbar-search" aria-controls="navbar-search"
                    aria-expanded="false"
                    class="md:hidden text-gray-500 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700 focus:outline-none focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-700 rounded-lg text-sm p-2.5 mr-1">
                    <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
                        viewBox="0 0 20 20">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z" />
                    </svg>
                    <span class="sr-only">Search</span>
                </button>
                <div class="relative hidden md:block">
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
            <div class="flex items-center md:order-2">
                <!-- User -->

                <!-- LANGUAGE -->
                <!-- <div class="flex flex-row items-center right-1 ml-4">
                    <a @click="language.setLang('TR')"
                        class="inline-flex items-center font-medium justify-center mx-1 text-sm text-gray-900 dark:text-white cursor-pointer">
                        <span class="items-center">
                            <img src="/src/assets/icons/tr.png"
                                class="w-6 h-6 border border-transparent hover:border-black dark:hover:border-white rounded-full transition duration-300 ease-in-out" />
                        </span>
                    </a>
                    <a @click="language.setLang('EN')"
                        class="inline-flex items-center font-medium justify-center mx-1 text-sm text-gray-900 dark:text-white cursor-pointer">
                        <span class="items-center">
                            <img src="/src/assets/icons/en.png"
                                class="w-6 h-6 border border-transparent hover:border-black dark:hover:border-white rounded-full transition duration-300 ease-in-out" />
                        </span>
                    </a>
                </div> -->
                <!-- LANGUAGE -->

                <!-- DARK & LIGHT MODE -->
                <!-- <div class="flex flex-row items-center right-1 ml-4">
                    <a @click="theme.toggleDark()"
                        class="inline-flex items-center font-medium justify-center mx-1 text-sm text-gray-900 dark:text-white cursor-pointer">
                        <span class="items-center">
                            <svg v-if="theme.isDark"
                                class="w-5 h-5 text-gray-800 dark:text-white hover:text-amber-500 dark:hover:text-amber-500"
                                aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor"
                                viewBox="0 0 20 20">
                                <path
                                    d="M10 15a5 5 0 1 0 0-10 5 5 0 0 0 0 10Zm0-11a1 1 0 0 0 1-1V1a1 1 0 0 0-2 0v2a1 1 0 0 0 1 1Zm0 12a1 1 0 0 0-1 1v2a1 1 0 1 0 2 0v-2a1 1 0 0 0-1-1ZM4.343 5.757a1 1 0 0 0 1.414-1.414L4.343 2.929a1 1 0 0 0-1.414 1.414l1.414 1.414Zm11.314 8.486a1 1 0 0 0-1.414 1.414l1.414 1.414a1 1 0 0 0 1.414-1.414l-1.414-1.414ZM4 10a1 1 0 0 0-1-1H1a1 1 0 0 0 0 2h2a1 1 0 0 0 1-1Zm15-1h-2a1 1 0 1 0 0 2h2a1 1 0 0 0 0-2ZM4.343 14.243l-1.414 1.414a1 1 0 1 0 1.414 1.414l1.414-1.414a1 1 0 0 0-1.414-1.414ZM14.95 6.05a1 1 0 0 0 .707-.293l1.414-1.414a1 1 0 1 0-1.414-1.414l-1.414 1.414a1 1 0 0 0 .707 1.707Z" />
                            </svg>
                            <svg v-if="!theme.isDark"
                                class="w-5 h-5 text-gray-800 dark:text-white hover:text-amber-500 dark:hover:text-amber-500"
                                aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor"
                                viewBox="0 0 18 20">
                                <path
                                    d="M17.8 13.75a1 1 0 0 0-.859-.5A7.488 7.488 0 0 1 10.52 2a1 1 0 0 0 0-.969A1.035 1.035 0 0 0 9.687.5h-.113a9.5 9.5 0 1 0 8.222 14.247 1 1 0 0 0 .004-.997Z" />
                            </svg>
                        </span>
                    </a>
                </div> -->
                <!-- DARK & LIGHT MODE -->
                <div class="relative inline-block text-left">

                    <button @click="toggleUser" id="dropdownAvatarButton" data-dropdown-toggle="dropdownAvatar"
                        class="flex mx-3 text-base rounded-full md:mr-0 focus:ring-4 focus:ring-gray-300 dark:focus:ring-gray-600"
                        type="button">
                        <span class="sr-only">Open user menu</span>
                        <img class="w-8 h-8 rounded-full" src="/src/assets/images/visitor.png" alt="visitor_photo">
                    </button>

                    <!-- Dropdown menu -->
                    <div ref="target" id="dropdownAvatar" :class="{ 'hidden': !userDropdown }"
                        class="origin-bottom-right z-10 absolute right-0 mt-2 w-48 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 focus:outline-none dark:bg-darkItemsColor dark:ring-gray-600">
                        <div class="py-1" role="menu" aria-orientation="vertical"
                            aria-labelledby="dropdownUserAvatarButton">
                            <div class="px-1 py-1 text-base text-gray-900 dark:text-white">
                                <RouterLink to="/profile/:slug"
                                    class="block px-4 py-2 font-sans text-base hover:underline text-gray-900 hover:text-sky-600 dark:text-white rounded-lg cursor-pointer hover:bg-gray-100 dark:hover:bg-gray-800 dark:hover:text-sky-600">
                                    <div>Fatih Kurt</div>
                                    <div class="font-sans text-sm truncate">@username</div>
                                </RouterLink>
                            </div>
                            <hr class="w-full h-px bg-gray-200 border-0 dark:bg-darkBgColor">
                            <ul>
                                <li class="py-1 px-1">
                                    <a href="#"
                                        class="block px-4 py-2 font-sans text-base hover:underline text-gray-900 hover:text-sky-600 dark:text-white rounded-lg cursor-pointer hover:bg-gray-100 dark:hover:bg-gray-800 dark:hover:text-sky-600">Dashboard</a>
                                </li>
                                <li class="py-1 px-1">
                                    <RouterLink to="/"
                                        class="block px-4 py-2 font-sans text-base hover:underline text-gray-900 hover:text-sky-600 dark:text-white rounded-lg cursor-pointer hover:bg-gray-100 dark:hover:bg-gray-800 dark:hover:text-sky-600">
                                        Reading List
                                    </RouterLink>
                                </li>
                                <li class="py-1 px-1">
                                    <RouterLink to="/settings/profile/member=:member-token"
                                        class="block px-4 py-2 font-sans text-base hover:underline text-gray-900 hover:text-sky-600 dark:text-white rounded-lg cursor-pointer hover:bg-gray-100 dark:hover:bg-gray-800 dark:hover:text-sky-600">
                                        {{ $t('settings') }}
                                    </RouterLink>
                                </li>
                                <hr class="w-full h-px bg-gray-200 border-0 dark:bg-darkBgColor">
                                <li class="py-1 px-1">
                                    <!-- sadece kullanici giris yapmamissa gozukecek -->
                                    <RouterLink to="/login"
                                        class="block px-4 py-2 font-sans text-base hover:underline text-gray-900 hover:text-sky-600 dark:text-white rounded-md cursor-pointer hover:bg-gray-100 dark:hover:bg-gray-800 dark:hover:text-sky-600">
                                        {{ $t('login') }}
                                    </RouterLink>
                                    <RouterLink to="/register"
                                        class="block px-4 py-2 font-sans text-base hover:underline text-gray-900 hover:text-sky-600 dark:text-white rounded-md cursor-pointer hover:bg-gray-100 dark:hover:bg-gray-800 dark:hover:text-sky-600">
                                        {{ $t('register') }}
                                    </RouterLink>
                                    <!-- sadece kullanici giris yapmamissa gozukecek -->
                                    <!-- sadece kullanici giris yapmissa gozukecek -->
                                    <!-- <RouterLink to="/login"
                                        class="block px-4 py-2 font-sans text-base hover:underline text-gray-900 hover:text-sky-600 dark:text-white rounded-md cursor-pointer hover:bg-gray-100 dark:hover:bg-gray-800 dark:hover:text-sky-600">
                                        {{ $t('sign-out') }}
                                    </RouterLink> -->
                                    <!-- sadece kullanici giris yapmissa gozukecek -->
                                </li>
                            </ul>
                        </div>
                    </div>
                    <!-- Dropdown menu -->

                </div>
                <!-- User -->

                <!-- MOBILE -->
                <button data-collapse-toggle="navbar-default" type="button" @click="toggleNavbar"
                    class="inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-800 dark:focus:ring-gray-600"
                    aria-controls="navbar-language" aria-expanded="false">
                    <span class="sr-only">Open main menu</span>
                    <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
                        viewBox="0 0 17 14">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M1 1h15M1 7h15M1 13h15" />
                    </svg>
                </button>
            </div>
            <div :class="{ 'hidden': !isNavbarOpen }"
                class="items-center justify-between sm:hidden w-full md:flex md:w-auto md:order-1" id="navbar-language">
                <ul
                    class="flex flex-col font-sans font-bold p-4 md:p-0 mt-4 border border-borderColor rounded-lg bg-lightItemsColor md:flex-row md:space-x-8 md:mt-0 md:border-0 md:bg-lightItemsColor dark:bg-darkItemsColor md:dark:bg-darkItemsColor dark:border-borderColor">
                    <li>
                        <RouterLink to="/web-development" active-class="dark:bg-blue-950 bg-gray-200"
                            class="inline-flex items-center font-sans font-semibold justify-center px-2 py-2 text-base text-black hover:text-sky-600 hover:underline dark:text-white rounded-lg cursor-pointer hover:bg-gray-200 dark:hover:bg-gray-800 dark:hover:text-sky-600"
                            aria-current="page">
                            {{ $t('web-development') }}
                        </RouterLink>
                    </li>
                    <li>
                        <RouterLink to="/trends" active-class="dark:bg-blue-950 bg-gray-200"
                            class="inline-flex items-center font-sans font-semibold justify-center px-2 py-2 text-base text-black hover:text-sky-600 hover:underline dark:text-white rounded-lg cursor-pointer hover:bg-gray-200 dark:hover:bg-gray-800 dark:hover:text-sky-600">
                            {{ $t('trends') }}
                        </RouterLink>
                    </li>
                    <li>
                        <RouterLink to="/developer-tools" active-class="dark:bg-blue-950 bg-gray-200"
                            class="inline-flex items-center font-sans font-semibold justify-center px-2 py-2 text-base text-black hover:text-sky-600 hover:underline dark:text-white rounded-lg cursor-pointer hover:bg-gray-200 dark:hover:bg-gray-800 dark:hover:text-sky-600">
                            {{ $t('developer-tools') }}
                        </RouterLink>
                    </li>
                    <li>
                        <RouterLink to="/discover" active-class="dark:bg-blue-950 bg-gray-200"
                            class="inline-flex items-center font-sans font-semibold justify-center px-2 py-2 text-base text-black hover:text-sky-600 hover:underline dark:text-white rounded-lg cursor-pointer hover:bg-gray-200 dark:hover:bg-gray-800 dark:hover:text-sky-600">
                            {{ $t('discover') }}
                        </RouterLink>
                    </li>
                    <li>
                        <RouterLink to="/contact" active-class="dark:bg-blue-950 bg-gray-200"
                            class="inline-flex items-center font-sans font-semibold justify-center px-2 py-2 text-base text-black hover:text-sky-600 hover:underline dark:text-white rounded-lg cursor-pointer hover:bg-gray-200 dark:hover:bg-gray-800 dark:hover:text-sky-600">
                            {{ $t('contact') }}
                        </RouterLink>
                    </li>
                </ul>
            </div>
            <!-- MOBILE -->
        </div>
    </nav>
</template>

<style scoped></style>