<script setup>

</script>

<template>
    <!-- subscribe -->
    <div class="flex my-4 bg-lightItemsColor dark:bg-darkItemsColor">
        <img src="../assets/images/gmail-subscribe.jpg" class="w-0 md:w-1/4 object-cover" />
        <div class="px-4 py-2">
            <h3 class="text-3xl text-gray-600 dark:text-white font-sans font-bold">{{ $t('subscribe-newsletter') }}</h3>
            <p class="text-xl text-gray-700 dark:text-white font-sans font-semibold">{{ $t('subscribe-desc') }}</p>
            <form class="mt-4 mb-10">
                <input type="email"
                    class="px-4 py-2 font-sans font-semibold text-sm text-gray-900 border border-gray-300 rounded-md bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-black dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                    :placeholder="$t('your-email')" />
                <button
                    class="px-4 py-2 text-white bg-lightBtnColor hover:bg-sky-600 dark:hover:bg-sky-700 rounded-md focus:ring-4 dark:bg-darkBtnColor dark:focus:ring-sky-800 focus:ring-blue-300">
                    {{ $t('subscribe-btn') }}
                    <i class='bx bx-right-arrow-alt'></i>
                </button>
                <p class="text-gray-900 dark:text-white opacity-50 text-sm mt-1">{{ $t('no-spam') }}</p>
            </form>
        </div>
    </div>
    <!-- ens subscribe section -->
</template>

<style lang="scss" scoped></style>