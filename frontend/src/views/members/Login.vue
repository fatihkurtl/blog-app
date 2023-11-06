<script setup>

</script>

<template>
    <section class="bg-white dark:bg-darkBgColor">
        <div class="py-8 px-4 mx-auto max-w-screen-xl lg:py-16 grid lg:grid-cols-2 gap-8 lg:gap-16">
            <div class="flex flex-col justify-center">
                <h1
                    class="mb-4 text-4xl font-extrabold tracking-tight leading-none text-gray-600 md:text-5xl lg:text-6xl dark:text-white">
                    {{ $t('login-banner') }}</h1>
                <p class="mb-6 text-lg font-sans font-normal text-gray-500 lg:text-xl dark:text-gray-400">
                    {{ $t('join-community') }}
                </p>
            </div>
            <div>
                <div class="w-full lg:max-w-xl p-6 space-y-8 sm:p-8 bg-lightItemsColor shadow-xl dark:bg-darkItemsColor">
                    <h2 class="text-2xl font-bold text-gray-600 dark:text-white">
                        {{ $t('login-to') }}
                    </h2>
                    <form class="mt-8 space-y-6" method="POST" enctype="multipart/form-data">
                        <div>
                            <label for="email"
                                class="block mb-2 text-sm font-sans font-semibold text-gray-600 dark:text-white">{{
                                    $t('e-mail') }}</label>
                            <input type="email" name="email" id="email"
                                class="bg-gray-50 border border-gray-300 text-gray-600 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-black dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                :placeholder="$t('e-mail-placeholder') + '@gmail.com'" required="">
                        </div>
                        <div>
                            <label for="password"
                                class="block mb-2 text-sm font-sans font-semibold text-gray-600 dark:text-white">{{
                                    $t('password') }}</label>
                            <input type="password" name="password" id="password" placeholder="••••••••"
                                class="bg-gray-50 border border-gray-300 text-gray-600 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-black dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                required>
                        </div>
                        <div class="flex items-start">
                            <div class="flex items-center h-5">
                                <input id="remember" aria-describedby="remember" name="remember" type="checkbox"
                                    class="w-4 h-4 border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-blue-300 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:bg-black dark:border-gray-600"
                                    required>
                            </div>
                            <div class="ml-3 text-sm">
                                <label for="remember" class="font-sans font-medium text-gray-500 dark:text-gray-400">
                                    {{ $t('remember-device') }}</label>
                            </div>
                            <RouterLink to="/reset-password"
                                class="ml-auto text-sm font-sans font-medium text-blue-600 hover:underline dark:text-blue-500">
                                {{ $t('forgot-password') }}</RouterLink>
                        </div>
                        <button type="submit"
                            class="w-full px-5 py-3 text-base font-sans font-medium text-center text-white bg-lightBtnColor hover:bg-sky-600 dark:hover:bg-sky-700 rounded-lg focus:ring-4 dark:bg-darkBtnColor dark:focus:ring-sky-800 focus:ring-blue-300 sm:w-auto">
                            {{ $t('login') }}
                        </button>
                        <div class="text-sm font-sans font-medium text-gray-500 dark:text-white">
                            {{ $t('not-a-member-yet') }}
                            <RouterLink to="/register" class="font-sans text-blue-600 hover:underline dark:text-blue-500">
                                {{ $t('create-account') }}</RouterLink>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </section>
</template>

<style lang="scss" scoped></style>