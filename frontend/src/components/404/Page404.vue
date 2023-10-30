<template>
    <main
        class="grid min-h-full place-items-center bg-lightItemsColor dark:bg-darkItemsColor px-6 py-24 my-4 mx-auto sm:py-32 lg:px-8">
        <div class="text-center">
            <p class="mb-4 text-7xl tracking-tight font-extrabold lg:text-9xl text-primary-600 dark:text-white">404</p>
            <h1 class="mt-4 text-3xl font-bold tracking-tight dark:text-white sm:text-5xl">{{ $t('page-not-found') }}</h1>
            <p class="mt-6 text-base leading-7 dark:text-gray-400">{{ $t('sorry') }}</p>
            <div class="mt-10 flex items-center justify-center gap-x-6">
                <RouterLink to="/"
                    class="rounded-md dark:bg-darkBtnColor bg-lightBtnColor hover:bg-sky-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">
                    {{$t('back-to-home')}}</RouterLink>
                <RouterLink to="/contact" class="text-sm font-semibold text-black dark:text-white">{{$t('support')}} <span
                        aria-hidden="true">&rarr;</span></RouterLink>
            </div>
        </div>
    </main>
</template>

<script setup>

</script>

<style lang="scss" scoped></style>