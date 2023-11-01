<script setup>
import Aside from '../../../../components/members/auth/Aside.vue';


</script>

<template>
    <main class="container mx-auto mt-4 min-w-full lg:px-0"> <!-- px-4 -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <!-- Content -->
            <form method="POST" enctype="multipart/form-data" class="col-span-2">
                <!-- Member -->
                <div class="bg-lightItemsColor dark:bg-darkItemsColor overflow-hidden mb-6 flex flex-col md:flex-row">
                    <div class="w-full p-4 md:w-2/3 lg:mx-4 lg:my-4 md:mx-4 md:my-4 sm:mx-1 sm:my-1">
                        <h2 class="text-xl md:text-2xl font-sans font-semibold text-gray-600 dark:text-white mb-2">
                            {{ $t('member') }} - 
                            <span class="text-sky-600 dark:text-sky-600">@username</span>
                        </h2>
                        <div>
                            <div class="mt-4">
                                <label for="fullName"
                                    class="block text-gray-600 dark:text-white text-sm font-sans font-semibold mb-2">
                                    {{ $t('fullname') }}
                                </label>
                                <input type="text" id="fullName" name="fullName" :placeholder="$t('fullname')"
                                    class="bg-gray-50 border border-gray-300 text-gray-600 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-black dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                            </div>
                            <div class="mt-4">
                                <label for="email"
                                    class="block text-gray-600 dark:text-white text-sm font-sans font-semibold mb-2"> {{
                                        $t('e-mail') }}
                                </label>
                                <input type="text" id="fullName" name="fullName" :placeholder="$t('e-mail')"
                                    class="bg-gray-50 border border-gray-300 text-gray-600 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-black dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                            </div>
                            <div class="mt-4">
                                <div class="flex items-center h-5">
                                    <input id="show-email" aria-describedby="show-email" name="show-email" type="checkbox"
                                        class="w-4 h-4 border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-blue-300 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:bg-black dark:border-gray-600">
                                    <label for="show-email" class="ml-2 font-sans text-gray-500 dark:text-gray-400">
                                        {{ $t('display-email') }}
                                    </label>
                                </div>
                            </div>
                            <div class="mt-4">
                                <label for="profilePhoto"
                                    class="block text-gray-600 dark:text-white text-sm font-sans font-semibold mb-2">
                                    {{ $t('profile-picture') }}
                                </label>
                                <div class="flex items-center mb-4">
                                    <img src="https://via.placeholder.com/64" alt="User Avatar"
                                        class="w-10 h-10 rounded-full mr-4">
                                    <input @change="" accept="image/*" max-file-size="3mb" file-upload
                                        class="block w-full text-sm text-gray-600 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-black dark:border-gray-600 dark:placeholder-gray-400"
                                        id="profilePhoto" type="file">
                                    <!-- <p :class="[photoErrorsObject.isActive === true ? photoErrorsObject : 'mt-1 text-sm font-sans text-gray-500 dark:text-white']"
                                        id="file_input_help">
                                        JPEG, PNG, JPG {{ $t('or') }} SVG (MAX. 3MB).
                                    </p> -->
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- Member -->
                <!-- Basic -->
                <div class="bg-lightItemsColor dark:bg-darkItemsColor overflow-hidden mb-6 flex flex-col md:flex-row">
                    <div class="w-full p-4 md:w-2/3 lg:mx-4 lg:my-4 md:mx-4 md:my-4 sm:mx-1 sm:my-1">
                        <h2 class="text-xl md:text-2xl font-sans font-semibold text-gray-600 dark:text-white mb-2">
                            {{ $t('basic') }}
                        </h2>
                        <div>
                            <div class="mt-4">
                                <label for="fullName"
                                    class="block text-gray-600 dark:text-white text-sm font-sans font-semibold mb-2">
                                    {{ $t('location') }}
                                </label>
                                <input type="text" id="location" name="location" :placeholder="$t('location-placeholder')"
                                    class="bg-gray-50 border border-gray-300 text-gray-600 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-black dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                            </div>
                            <div class="mt-4">
                                <label for="bio"
                                    class="block text-gray-600 dark:text-white text-sm font-sans font-semibold mb-2">
                                    {{ $t('bio') }}
                                </label>
                                <textarea
                                    class="resize-none w-full h-24 py-2 px-4 border dark:bg-darkBgColor dark:text-white text-gray-600 border-gray-500 rounded-lg focus:outline-none focus:border-gray-300"
                                    :placeholder="$t('bio-placeholder')" />
                            </div>
                        </div>
                    </div>
                </div>
                <!-- Basic -->
                <!-- Save Button -->
                <div class="bg-lightItemsColor dark:bg-darkItemsColor overflow-hidden mb-6">
                    <div class="w-full p-4 md:w-2/3 lg:mx-4 lg:my-4 md:mx-4 md:my-4 sm:mx-1 sm:my-1">
                        <button type="submit"
                            class="min-w-full px-5 py-3 text-base font-sans text-center text-white bg-lightBtnColor hover:bg-sky-600 dark:hover:bg-sky-700 rounded-lg focus:ring-4 focus:ring-blue-300 sm:w-auto dark:bg-darkBtnColor dark:focus:ring-sky-800">
                            {{ $t('save-profile-btn') }}
                        </button>
                    </div>
                </div>
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