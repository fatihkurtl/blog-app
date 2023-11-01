<script setup>
import { ref } from 'vue';
import { useThemeStore } from '../../../../stores/theme';
import { useLangStore } from '../../../../stores/language';
import Aside from '../../../../components/members/auth/Aside.vue';


const theme = useThemeStore();
const language = useLangStore();

const lang = ref(localStorage.getItem('lang'));

</script>

<template>
    <main class="container mx-auto mt-4 min-w-full lg:px-0"> <!-- px-4 -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <!-- Customizatiom -->
            <form method="POST" enctype="multipart/form-data" class="col-span-2">
                <div class="bg-lightItemsColor dark:bg-darkItemsColor overflow-hidden mb-6 flex flex-col md:flex-row">
                    <div class="w-full p-4 md:w-2/3 lg:mx-4 lg:my-4 md:mx-4 md:my-4 sm:mx-1 sm:my-1">
                        <h2 class="text-xl md:text-2xl font-sans font-semibold text-gray-600 dark:text-white mb-2">
                            {{ $t('appearance') }} -
                            <span class="text-sky-600 dark:text-sky-600">@username</span>
                        </h2>
                        <div class="mt-4">
                            <!-- Theme Settings -->
                            <span class="text-md md:text-md font-sans font-semibold text-gray-600 dark:text-white">
                                {{ $t('site-theme') }}
                            </span>
                            <ul class="grid w-full gap-6 md:grid-cols-2 mt-2">
                                <li>
                                    <input type="radio" id="light-theme" name="light-theme" value="light-theme"
                                        class="hidden peer" required>
                                    <label @click="theme.isDark && theme.toggleDark()" for="light-theme"
                                    :class="[!theme.isDark ? 'border-amber-500 dark:border-amber-500' : 'border-gray-200 dark:border-gray-700']"
                                        class="inline-flex items-center justify-between w-full p-5 text-gray-500 bg-white border rounded-lg cursor-pointer dark:hover:text-gray-300 hover:text-gray-600 hover:bg-gray-100 dark:text-gray-400 dark:bg-darkItemsColor dark:hover:bg-gray-700">
                                        <div class="block">
                                            <div class="w-full text-lg font-semibold">{{ $t('light-theme') }}</div>
                                        </div>
                                        <svg :class="!theme.isDark && 'text-amber-500 dark:text-amber-500'" class="w-6 h-6" aria-hidden="true"
                                            xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                                            <path
                                                d="M10 15a5 5 0 1 0 0-10 5 5 0 0 0 0 10Zm0-11a1 1 0 0 0 1-1V1a1 1 0 0 0-2 0v2a1 1 0 0 0 1 1Zm0 12a1 1 0 0 0-1 1v2a1 1 0 1 0 2 0v-2a1 1 0 0 0-1-1ZM4.343 5.757a1 1 0 0 0 1.414-1.414L4.343 2.929a1 1 0 0 0-1.414 1.414l1.414 1.414Zm11.314 8.486a1 1 0 0 0-1.414 1.414l1.414 1.414a1 1 0 0 0 1.414-1.414l-1.414-1.414ZM4 10a1 1 0 0 0-1-1H1a1 1 0 0 0 0 2h2a1 1 0 0 0 1-1Zm15-1h-2a1 1 0 1 0 0 2h2a1 1 0 0 0 0-2ZM4.343 14.243l-1.414 1.414a1 1 0 1 0 1.414 1.414l1.414-1.414a1 1 0 0 0-1.414-1.414ZM14.95 6.05a1 1 0 0 0 .707-.293l1.414-1.414a1 1 0 1 0-1.414-1.414l-1.414 1.414a1 1 0 0 0 .707 1.707Z" />
                                        </svg>
                                    </label>
                                </li>
                                <li>
                                    <input type="radio" id="dark-theme" name="dark-theme" value="dark-theme"
                                        class="hidden peer">
                                    <label @click="!theme.isDark && theme.toggleDark()" for="dark-theme"
                                    :class="[theme.isDark ? 'border-amber-500 dark:border-amber-500' : 'border-gray-200 dark:border-gray-700']"
                                        class="inline-flex items-center justify-between w-full p-5 text-gray-500 bg-white border rounded-lg cursor-pointer dark:hover:text-gray-300 hover:text-gray-600 hover:bg-gray-100 dark:text-gray-400 dark:bg-darkItemsColor dark:hover:bg-gray-700">
                                        <div class="block">
                                            <div class="w-full text-lg font-semibold">{{ $t('dark-theme') }}</div>
                                        </div>
                                        <svg :class="[theme.isDark && 'text-amber-500 dark:text-amber-500']" class="w-6 h-6" aria-hidden="true"
                                            xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 18 20">
                                            <path
                                                d="M17.8 13.75a1 1 0 0 0-.859-.5A7.488 7.488 0 0 1 10.52 2a1 1 0 0 0 0-.969A1.035 1.035 0 0 0 9.687.5h-.113a9.5 9.5 0 1 0 8.222 14.247 1 1 0 0 0 .004-.997Z" />
                                        </svg>
                                    </label>
                                </li>
                            </ul>
                            <!-- Theme Settings -->
                        </div>
                    </div>
                </div>
                <!-- Customizatiom -->

                <!-- Language -->
                <div class="bg-lightItemsColor dark:bg-darkItemsColor overflow-hidden mb-6 flex flex-col md:flex-row">
                    <div class="w-full p-4 md:w-2/3 lg:mx-4 lg:my-4 md:mx-4 md:my-4 sm:mx-1 sm:my-1">
                        <h2 class="text-xl md:text-2xl font-sans font-semibold text-gray-600 dark:text-white mb-2">
                            {{ $t('localization') }}
                        </h2>
                        <div class="mt-4">
                            <!-- Language Settings -->
                            <span class="text-md md:text-md font-sans font-semibold text-gray-600 dark:text-white">
                                {{ $t('site-language') }}
                            </span>
                            <ul class="grid w-full gap-6 md:grid-cols-2 mt-2">
                                <li>
                                    <input type="radio" id="lang-tr" name="lang-tr" value="lang-tr" class="hidden peer"
                                        required>
                                    <label @click="lang !== 'TR' && language.setLang('TR')" for="lang-tr"
                                    :class="[lang === 'TR' ? 'border-amber-500 dark:border-amber-500' : 'border-gray-200 dark:border-gray-700']"
                                        class="inline-flex items-center justify-between w-full p-5 text-gray-500 bg-white border rounded-lg cursor-pointer dark:hover:text-gray-300 hover:text-gray-600 hover:bg-gray-100 dark:text-gray-400 dark:bg-darkItemsColor dark:hover:bg-gray-700">
                                        <div class="block">
                                            <div class="w-full text-lg font-semibold">{{ $t('turkish') }}</div>
                                        </div>
                                        <span class="items-center">
                                            <img src="/src/assets/icons/tr.png"
                                                class="w-6 h-6 border border-transparent hover:border-black dark:hover:border-white rounded-full transition duration-300 ease-in-out" />
                                        </span>
                                    </label>
                                </li>
                                <li>
                                    <input type="radio" id="lang-en" name="lang-en" value="lang-en" class="hidden peer">
                                    <label @click="lang !== 'EN' && language.setLang('EN')" for="lang-en"
                                    :class="[lang === 'EN' ? 'border-amber-500 dark:border-amber-500' : 'border-gray-200 dark:border-gray-700']"
                                        class="inline-flex items-center justify-between w-full p-5 text-gray-500 bg-white border rounded-lg cursor-pointer dark:hover:text-gray-300 hover:text-gray-600 hover:bg-gray-100 dark:text-gray-400 dark:bg-darkItemsColor dark:hover:bg-gray-700">
                                        <div class="block">
                                            <div class="w-full text-lg font-semibold">{{ $t('english') }}</div>
                                        </div>
                                        <span class="items-center">
                                            <img src="/src/assets/icons/en.png"
                                                class="w-6 h-6 border border-transparent hover:border-black dark:hover:border-white rounded-full transition duration-300 ease-in-out" />
                                        </span>
                                    </label>
                                </li>
                            </ul>
                            <!-- Language Settings -->
                        </div>
                    </div>
                </div>
                <!-- Language -->
                <!-- Save Button -->
                <!-- <div class="bg-lightItemsColor dark:bg-darkItemsColor overflow-hidden mb-6">
                    <div class="w-full p-4 md:w-2/3 lg:mx-4 lg:my-4 md:mx-4 md:my-4 sm:mx-1 sm:my-1">
                        <button type="submit"
                            class="min-w-full px-5 py-3 text-base font-sans text-center text-white bg-lightBtnColor hover:bg-sky-600 dark:hover:bg-sky-700 rounded-lg focus:ring-4 focus:ring-blue-300 sm:w-auto dark:bg-darkBtnColor dark:focus:ring-sky-800">
                            {{ $t('save') }}
                        </button>
                    </div>
                </div> -->
                <!-- Save Button -->
            </form>
            <!-- Content -->

            <!-- Aside -->
            <Aside />
            <!-- Aside -->
        </div>
        <br>
    </main>
</template>

<style lang="scss" scoped></style>