<script setup>
import { ref, computed } from 'vue';
import { useMouseInElement } from '@vueuse/core';
import { useRoute } from 'vue-router';

const route = useRoute();

const target = ref(null);

const { elementX, elementY, isOutside, elementHeight, elementWidth } = useMouseInElement(target);

const svgTransform = computed(() => {
    // const MAX_ROTATION = 6
    const MAX_ROTATION = 10

    const rX = (
        MAX_ROTATION / 2 - (elementY.value / elementHeight.value) * MAX_ROTATION
    ).toFixed(2);

    const rY = (
        // MAX_ROTATION / 2 - (elementX.value / elementWidth.value) * MAX_ROTATION - MAX_ROTATION / 2
        MAX_ROTATION / 2 - (elementX.value / elementWidth.value) * MAX_ROTATION
    ).toFixed(2);

    return isOutside.value ? '' : `perspective(${elementWidth.value}px) rotateX(${rX}deg) rotateY(${rY}deg)`
});

</script>

<template>
    <section class="my-4"> <!-- bg-lightItemsColor dark:bg-darkItemsColor -->
        <div class="grid max-w-screen-xl px-4 py-8 mx-auto lg:gap-8 xl:gap-0 lg:py-16 lg:grid-cols-12">
            <div class="mr-auto place-self-center lg:col-span-7">

                <h1
                    class="max-w-2xl mb-4 text-4xl font-extrabold tracking-tight leading-none md:text-5xl xl:text-6xl text-gray-900 dark:text-white">
                    {{ $t('banner-header') }}
                </h1>

                <p
                    class="max-w-2xl mb-6 font-sans font-normal lg:mb-8 md:text-lg lg:text-xl text-gray-500 dark:text-gray-400">
                    {{ $t('banner-desc') }}
                </p>

                <RouterLink to="/discover"
                    class="inline-flex items-center justify-center px-5 py-3 mr-3 text-sans font-semibold text-center text-black hover:text-sky-600 hover:underline dark:text-white rounded-lg cursor-pointer hover:bg-gray-200 dark:hover:bg-gray-800 dark:hover:text-sky-600">
                    {{ $t('explore-now') }}
                    <svg class="w-5 h-5 ml-2 -mr-1" fill="currentColor" viewBox="0 0 20 20"
                        xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd"
                            d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
                            clip-rule="evenodd"></path>
                    </svg>
                </RouterLink>

                <a href="#"
                    class="inline-flex items-center justify-center px-5 py-3 text-sans font-semibold text-center text-black hover:text-sky-600 hover:underline dark:text-white rounded-lg cursor-pointer hover:bg-gray-200 dark:hover:bg-gray-800 dark:hover:text-sky-600">
                    Connect with Developers
                </a>

            </div>

            <div class="hidden lg:mt-0 lg:col-span-5 lg:flex"
                :style="{ transform: svgTransform, transition: 'transform 0.25s ease-out' }">
                <img ref="target" v-if="route.name == 'Home'" src="/src/assets/logo.svg" alt="vue logo">
                <!-- <h1
                ref="target"
                v-if="route.name == 'Web Dev'"
                    class="max-w-2xl mb-4 text-4xl font-extrabold tracking-tight leading-none md:text-5xl xl:text-6xl text-gray-900 dark:text-white">
                    {{ $t('web-development') }}
                </h1>
                <h1
                ref="target"
                v-if="route.name == 'Trends'"
                    class="max-w-2xl mb-4 text-4xl font-extrabold tracking-tight leading-none md:text-5xl xl:text-6xl text-gray-900 dark:text-white">
                    {{ $t('trends') }}
                </h1>
                <h1
                ref="target"
                v-if="route.name == 'Dev Tools'"
                    class="max-w-2xl mb-4 text-4xl font-extrabold tracking-tight leading-none md:text-5xl xl:text-6xl text-gray-900 dark:text-white">
                    {{ $t('developer-tools') }}
                </h1> -->
                <!-- <h1 ref="target" v-if="route.name == 'Dev Tools'"
                    class="max-w-2xl mb-4 text-4xl font-extrabold tracking-tight leading-none md:text-5xl xl:text-6xl text-transparent dark:text-transparent bg-clip-text dark:bg-clip-text bg-gradient-to-r dark:bg-gradient-to-r from-purple-500 dark:from-purple-500 via-blue-500 dark:via-blue-500 to-green-500 dark:to-green-500 dark:text-white">
                    {{ $t('developer-tools') }}
                </h1> -->
            </div>
        </div>
    </section>
</template>

<style lang="scss" scoped></style>