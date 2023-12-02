<script setup>
defineProps({
    error: Object
});
</script>

<template>
    <section class="col-span-2">
        <div class="mt-4">
            <h2 class="mb-4 text-2xl tracking-tight font-extrabold text-center text-gray-900 dark:text-white">
                {{ $t('error-loading-articles') }}
            </h2>
            <p class="mb-8 lg:mb-16 font-sans font-semibold text-center text-gray-500 dark:text-gray-400 sm:text-xl">
                {{ error }}
            </p>
        </div>
    </section>
</template>

<style lang="scss" scoped></style>