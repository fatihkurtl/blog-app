<script setup>

</script>

<template>
    <footer class="bg-lightItemsColor dark:bg-darkItemsColor">
        <div class="mx-auto w-full max-w-screen-xl p-4 py-6 lg:py-8">
            <div class="md:flex md:justify-between">
                <div class="mb-6 md:mb-0">
                    <RouterLink to="/" class="flex items-center">
                        <img src="../assets//logo.svg" class="h-8 mr-3" alt="Vue Logo" />
                        <span
                            class="self-center text-2xl font-bold whitespace-nowrap text-black dark:text-white">./fullstack
                            <span class="text-sm font-semibold text-gray-400 dark:text-gray-500">v0.1.0</span>
                        </span>
                    </RouterLink>
                    <!-- Enail Subscribe -->
                    <div class="max-w-xs my-9">
                        <h4 class="mb-2 text-lg font-semibold text-gray-600 dark:text-white">
                            {{ $t('subscribe-newsletter') }}
                        </h4>
                        <form action="#" method="post" class="flex">
                            <input type="email" name="email" :placeholder="$t('your-email')"
                                class="w-full p-2 mr-2 text-gray-600 text-sm font-sans font-semibold dark:text-white bg-gray-50 dark:bg-black border rounded-l focus:outline-none focus:border-blue-300">
                            <button type="submit"
                                class="p-2 rounded-r font-sans font-semibold text-white bg-lightBtnColor hover:bg-sky-600 dark:hover:bg-sky-700 focus:ring-4 dark:bg-darkBtnColor dark:focus:ring-sky-800 focus:ring-blue-300">
                                {{ $t('subscribe-btn') }}
                            </button>
                        </form>
                    </div>
                    <!-- Enail Subscribe -->
                </div>
                <div class="grid grid-cols-2 gap-8 sm:gap-6 sm:grid-cols-3 lg:grid-cols-4 md:grid-cols-4 lg:gap-9 md:gap-9">
                    <div>
                        <h2 class="mb-6 text-sm font-sans font-bold text-black uppercase dark:text-white">
                            {{ $t('resources') }}</h2>
                        <ul class="text-gray-500 dark:text-gray-400 font-medium">
                            <li class="mb-4">
                                <a href="https://flowbite.com/" target="_blank" class="hover:underline">Flowbite</a>
                            </li>
                            <li>
                                <a href="https://tailwindcss.com/" target="_blank" class="hover:underline">Tailwind CSS</a>
                            </li>
                        </ul>
                    </div>
                    <div>
                        <h2 class="mb-6 text-sm font-sans font-bold text-black uppercase dark:text-white">
                            {{ $t('follow-us') }}
                        </h2>
                        <ul class="text-gray-500 dark:text-gray-400 font-medium">
                            <li class="mb-4">
                                <a href="https://github.com/fatihkurtl" target="_blank" class="hover:underline ">Github</a>
                            </li>
                            <li>
                                <a href="https://www.linkedin.com/in/fatihkurtl/" target="_blank"
                                    class="hover:underline">Linkedin</a>
                            </li>
                        </ul>
                    </div>
                    <div>
                        <h2 class="mb-6 text-sm font-sans font-bold text-black uppercase dark:text-white">
                            {{ $t('categories') }}</h2>
                        <ul class="text-gray-500 dark:text-gray-400 font-medium">
                            <li class="mb-4">
                                <RouterLink to="/web_dev" class="hover:underline">{{ $t('web-development') }}</RouterLink>
                            </li>
                            <li class="mb-4">
                                <RouterLink to="/trends" class="hover:underline">{{ $t('trends') }}</RouterLink>
                            </li>
                            <li class="mb-4">
                                <RouterLink to="/dev_tools" class="hover:underline">{{ $t('developer-tools') }}</RouterLink>
                            </li>
                            <li class="mb-4">
                                <RouterLink to="/discover" class="hover:underline">{{ $t('discover') }}</RouterLink>
                            </li>
                        </ul>
                    </div>
                    <div>
                        <h2 class="mb-6 text-sm font-sans font-bold text-black uppercase dark:text-white">{{ $t('legal') }}
                        </h2>
                        <ul class="text-gray-500 dark:text-gray-400 font-medium">
                            <li class="mb-4">
                                <RouterLink to="/terms-and-conditions" class="hover:underline">{{ $t('terms-conditions') }}
                                </RouterLink>
                            </li>
                            <li class="mb-4">
                                <RouterLink to="/privacy-policy" class="hover:underline">{{ $t('privacy-policy') }}
                                </RouterLink>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
            <hr class="my-6 border-gray-200 sm:mx-auto dark:border-gray-700 lg:my-8" />
            <div class="sm:flex sm:items-center sm:justify-between">
                <span class="text-sm text-gray-500 sm:text-center dark:text-gray-400">© 2023 <a href="https://flowbite.com/"
                        class="hover:underline">./fullstack™</a>. {{ $t('rights') }}
                </span>
                <div class="flex mt-4 space-x-5 sm:justify-center sm:mt-0">
                    <a href="https://github.com/fatihkurtl" target="_blank"
                        class="text-gray-500 hover:text-gray-900 dark:hover:text-white">
                        <svg class="w-4 h-4" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor"
                            viewBox="0 0 20 20">
                            <path fill-rule="evenodd"
                                d="M10 .333A9.911 9.911 0 0 0 6.866 19.65c.5.092.678-.215.678-.477 0-.237-.01-1.017-.014-1.845-2.757.6-3.338-1.169-3.338-1.169a2.627 2.627 0 0 0-1.1-1.451c-.9-.615.07-.6.07-.6a2.084 2.084 0 0 1 1.518 1.021 2.11 2.11 0 0 0 2.884.823c.044-.503.268-.973.63-1.325-2.2-.25-4.516-1.1-4.516-4.9A3.832 3.832 0 0 1 4.7 7.068a3.56 3.56 0 0 1 .095-2.623s.832-.266 2.726 1.016a9.409 9.409 0 0 1 4.962 0c1.89-1.282 2.717-1.016 2.717-1.016.366.83.402 1.768.1 2.623a3.827 3.827 0 0 1 1.02 2.659c0 3.807-2.319 4.644-4.525 4.889a2.366 2.366 0 0 1 .673 1.834c0 1.326-.012 2.394-.012 2.72 0 .263.18.572.681.475A9.911 9.911 0 0 0 10 .333Z"
                                clip-rule="evenodd" />
                        </svg>
                        <span class="sr-only">GitHub account</span>
                    </a>
                    <a href="https://www.linkedin.com/in/fatihkurtl/" target="_blank"
                        class="text-gray-500 hover:text-gray-900 dark:hover:text-white">
                        <svg class="w-4 h-4" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor"
                            viewBox="0 0 15 15">
                            <path fill-rule="evenodd"
                                d="M7.979 5v1.586a3.5 3.5 0 0 1 3.082-1.574C14.3 5.012 15 7.03 15 9.655V15h-3v-4.738c0-1.13-.229-2.584-1.995-2.584-1.713 0-2.005 1.23-2.005 2.5V15H5.009V5h2.97ZM3 2.487a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Z"
                                clip-rule="evenodd" />
                            <path d="M3 5.012H0V15h3V5.012Z" />
                        </svg>
                        <span class="sr-only">linkedin account</span>
                    </a>
                </div>
            </div>
        </div>
    </footer>

    <!-- <footer class="bg-white shadow mt-2 dark:bg-darkItemsColor py-10">
        <div class="px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between">
                <div>
                    <h3 class="text-lg font-bold text-white">Blog Site</h3>
                    <p class="text-gray-300/50">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla imperdiet
                        lectus
                        urna,
                        at efficitur nunc bibendum sed.</p>
                </div>
                <div>
                    <h3 class="text-lg font-bold text-white">Contact</h3>
                    <p class="text-gray-300/50">Email: info@blogsite.com</p>
                    <p class="text-gray-300/50">Phone: +1 123 456 7890</p>
                </div>
                <div>
                    <h3 class="text-lg font-bold text-white">Follow</h3>
                    <div class="text-gray-300/50 col-span flex items-center gap-x-2 mt-2">
                    <a href="https://github.com/fatihkurtl" target="_blank" class="text-gray-300/50 hover:text-white">
                        <svg class="w-6 h-6" aria-hidden="true"
                            xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                            <path fill-rule="evenodd"
                                d="M10 .333A9.911 9.911 0 0 0 6.866 19.65c.5.092.678-.215.678-.477 0-.237-.01-1.017-.014-1.845-2.757.6-3.338-1.169-3.338-1.169a2.627 2.627 0 0 0-1.1-1.451c-.9-.615.07-.6.07-.6a2.084 2.084 0 0 1 1.518 1.021 2.11 2.11 0 0 0 2.884.823c.044-.503.268-.973.63-1.325-2.2-.25-4.516-1.1-4.516-4.9A3.832 3.832 0 0 1 4.7 7.068a3.56 3.56 0 0 1 .095-2.623s.832-.266 2.726 1.016a9.409 9.409 0 0 1 4.962 0c1.89-1.282 2.717-1.016 2.717-1.016.366.83.402 1.768.1 2.623a3.827 3.827 0 0 1 1.02 2.659c0 3.807-2.319 4.644-4.525 4.889a2.366 2.366 0 0 1 .673 1.834c0 1.326-.012 2.394-.012 2.72 0 .263.18.572.681.475A9.911 9.911 0 0 0 10 .333Z"
                                clip-rule="evenodd" />
                        </svg>
                    </a>
                    <a href="https://www.linkedin.com/in/fatihkurtl/" target="_blank" class="text-gray-300/50 hover:text-blue-700">
                        <svg class="w-6 h-6" aria-hidden="true"
                            xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 15 15">
                            <path fill-rule="evenodd"
                                d="M7.979 5v1.586a3.5 3.5 0 0 1 3.082-1.574C14.3 5.012 15 7.03 15 9.655V15h-3v-4.738c0-1.13-.229-2.584-1.995-2.584-1.713 0-2.005 1.23-2.005 2.5V15H5.009V5h2.97ZM3 2.487a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Z"
                                clip-rule="evenodd" />
                            <path d="M3 5.012H0V15h3V5.012Z" />
                        </svg>
                    </a>
                    </div>
                </div>
            </div>
            <div class="mt-2">
                <p class="text-gray-300/50">© 2021 ./fullstack™. All rights reserved.</p>
            </div>
        </div>
    </footer> -->


    <!-- <footer class="bg-white shadow mt-2 dark:bg-darkItemsColor py-2">
        <div class="w-full mx-auto max-w-screen-xl p-4 md:flex md:items-center md:justify-between">
            <span class="text-sm text-gray-500 sm:text-center dark:text-gray-400">© 2023 <a href="https://flowbite.com/"
                    class="hover:underline">./fullstack™</a>. All Rights Reserved.
            </span>            
        </div>
    </footer> -->
    <!-- <h1 class="text-black dark:text-white">Footer</h1> -->
</template>

<style scoped></style>