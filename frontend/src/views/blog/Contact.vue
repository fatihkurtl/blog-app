<script setup>

</script>

<template>
    <main class="container mx-auto mt-4 mb-4 lg:px-0 min-w-full"> <!-- px-4 -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <section class="bg-lightItemsColor dark:bg-darkItemsColor col-span-5">
                <div class="py-8 lg:py-16 px-4 mx-auto max-w-screen-md">
                    <h2 class="mb-4 text-4xl tracking-tight font-extrabold text-center text-black dark:text-white">
                        {{$t('contact-us')}}
                    </h2>
                    <p class="mb-8 lg:mb-16 font-light text-center text-gray-500 dark:text-gray-400 sm:text-xl">
                        {{$t('contact-desc')}}
                    </p>
                    <form action="#" class="space-y-8">
                        <div>
                            <label for="email"
                                class="block mb-2 text-sm font-sans font-semibold text-gray-900 dark:text-gray-300">{{$t('e-mail')}}</label>
                            <input type="email" id="email"
                                class="shadow-sm font-sans font-semibold bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-black dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500 dark:shadow-sm-light"
                                :placeholder="$t('e-mail-placeholder') + '@gmail.com'" required>
                        </div>
                        <div>
                            <label for="subject"
                                class="block mb-2 text-sm font-sans font-semibold text-white dark:text-gray-300">{{$t('subject')}}</label>
                            <input type="text" id="subject"
                                class="block p-3 w-full text-sm text-white font-sans font-semibold bg-gray-50 rounded-lg border border-gray-300 shadow-sm focus:ring-primary-500 focus:border-primary-500 dark:bg-black dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500 dark:shadow-sm-light"
                                :placeholder="$t('subject-placeholder')" required>
                        </div>
                        <div class="sm:col-span-2">
                            <label for="message"
                                class="block mb-2 text-sm font-sans font-semibold text-gray-900 dark:text-gray-300">{{$t('message')}}</label>
                            <textarea id="message" rows="6"
                                class="block resize-none p-2.5 w-full text-sm font-sans font-semibold text-white bg-gray-50 rounded-lg shadow-sm border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-black dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                                :placeholder="$t('message-placeholder')"></textarea>
                        </div>
                        <button type="submit"
                            class="py-3 px-5 text-sm font-sans font-semibold text-center text-white rounded-lg sm:w-fit bg-lightBtnColor hover:bg-sky-600 dark:bg-darkBtnColor dark:hover:bg-sky-700 dark:focus:ring-sky-800 focus:ring-4 focus:outline-none focus:ring-primary-300">
                            {{$t('send-message-btn')}}</button>
                    </form>
                </div>
            </section>
        </div>
    </main>
</template>

<style scoped></style>