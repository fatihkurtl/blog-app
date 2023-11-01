<script setup>
import Aside from '../../../../components/members/auth/Aside.vue';
</script>

<template>
    <main class="container mx-auto mt-4 min-w-full lg:px-0"> <!-- px-4 -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">

            <!-- Content -->
            <form method="POST" enctype="multipart/form-data" class="col-span-2">
                <!-- Set Password -->
                <div class="bg-lightItemsColor dark:bg-darkItemsColor overflow-hidden mb-6 flex flex-col md:flex-row">
                    <div class="w-full p-4 md:w-2/3 lg:mx-4 lg:my-4 md:mx-4 md:my-4 sm:mx-1 sm:my-1">
                        <h2 class="text-xl md:text-2xl font-sans font-semibold text-gray-600 dark:text-white mb-2">
                            {{ $t('account') }} -
                            <span class="text-sky-600 dark:text-sky-600">@username</span>
                        </h2>
                        <h4 class="text-xl md:text-xl font-sans font-semibold text-gray-600 dark:text-white py-4">
                            {{ $t('set-new-password') }}
                        </h4>
                        <div>
                            <div class="mt-4">
                                <label for="current-password"
                                    class="block mb-2 text-sm font-sans font-semibold text-gray-600 dark:text-white">
                                    {{ $t('current-password') }}
                                </label>
                                <input type="password" name="current-password" id="current-password" placeholder="••••••••"
                                    class="bg-gray-50 border border-gray-300 text-gray-600 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-black dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                    required>
                            </div>
                            <div class="mt-4">
                                <label for="password"
                                    class="block mb-2 text-sm font-sans font-semibold text-gray-600 dark:text-white">
                                    {{ $t('password') }}
                                </label>
                                <input type="password" name="password" id="password" placeholder="••••••••"
                                    class="bg-gray-50 border border-gray-300 text-gray-600 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-black dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                    required>
                            </div>
                            <div class="mt-4">
                                <label for="confirm-new-password"
                                    class="block mb-2 text-sm font-sans font-semibold text-gray-600 dark:text-white">
                                    {{ $t('confirm-new-password') }}
                                </label>
                                <input type="password" name="confirm-new-password" id="confirm-new-password"
                                    placeholder="••••••••"
                                    class="bg-gray-50 border border-gray-300 text-gray-600 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-black dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                    required>
                            </div>
                            <div class="mt-4">
                                <button type="submit"
                                    class="px-5 py-3 text-base font-sans text-center text-white bg-lightBtnColor hover:bg-sky-600 dark:hover:bg-sky-700 rounded-lg focus:ring-4 focus:ring-blue-300 sm:w-auto dark:bg-darkBtnColor dark:focus:ring-sky-800">
                                    {{ $t('save-profile-btn') }}
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- Set Password -->
                <!-- Account Emails -->
                <div class="bg-lightItemsColor dark:bg-darkItemsColor overflow-hidden mb-6 flex flex-col md:flex-row">
                    <div class="w-full p-4 md:w-2/3 lg:mx-4 lg:my-4 md:mx-4 md:my-4 sm:mx-1 sm:my-1">
                        <h2 class="text-xl md:text-2xl font-sans font-semibold text-gray-600 dark:text-white mb-2">
                            {{ $t('account-emails') }}
                        </h2>
                        <h4 class="text-md md:text-md font-sans font-semibold text-gray-400 dark:text-gray-500 py-4">
                            {{ $t('primary-email') }}
                            <span class="text-sky-600 dark:text-sky-600 mx-1">user_email@gmail.com</span>
                        </h4>
                    </div>
                </div>
                <!-- Account Emails -->
            </form>

            <!-- Aside -->
            <Aside />
            <!-- Aside -->

            <!-- Danger Zone -->
            <div
                class="bg-lightItemsColor dark:bg-darkItemsColor overflow-hidden mb-6 flex flex-col md:flex-row col-span-2">
                <div class="w-full p-4 md:w-2/3 lg:mx-4 lg:my-4 md:mx-4 md:my-4 sm:mx-1 sm:my-1">
                    <h2 class="text-xl md:text-2xl font-sans font-semibold text-red-600 dark:text-red-600 mb-2">
                        {{ $t('danger-zone') }}
                    </h2>
                    <h4 class="text-xl md:text-xl font-sans font-semibold text-gray-600 dark:text-white py-4">
                        {{ $t('delete-account') }}
                    </h4>
                    <div class="w-3/4">
                        <div
                            class="whitespace-normal text-sm md:text-sm font-sans font-semibold text-gray-600 dark:text-white">
                            {{ $t('delete-account-desc') }}
                            <br />
                            {{ $t('delete-account-desc2') }}
                        </div>
                    </div>
                    <div class="mt-4">
                        <button type="delete"
                            class="px-5 py-3 text-base font-sans text-center text-white bg-red-600 hover:bg-red-500 dark:bg-red-600 dark:hover:bg-red-700 rounded-lg focus:ring-4 focus:ring-red-300 sm:w-auto dark:focus:ring-red-800">
                            {{ $t('delete-account') }}
                        </button>
                    </div>
                    <div class="mt-4">
                        <span class="text-gray-600 dark:text-white">
                            {{ $t('any-questions') }}
                            <RouterLink to="/contact" class="text-sky-600 hover:underline dark:text-sky-600 mx-1">
                                {{ $t('contact-us') }}
                            </RouterLink>
                        </span>
                    </div>
                </div>
            </div>
            <!-- Danger Zone -->
            <!-- Content -->
        </div>

        <br>
    </main>
</template>

<style lang="scss" scoped></style>