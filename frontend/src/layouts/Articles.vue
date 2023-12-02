<script setup>
import { ref } from 'vue';
import { useFetch } from '../composables/services/articles.get';
import ArticleSkeleton from '../components/skeletons/ArticleSkeleton.vue';
import ArticleErrors from '../components/errors/ArticleErrors.vue';
import Pagination from './Pagination.vue';

const { response, loading, error } = useFetch('/products');


</script>

<template>
    <ArticleErrors v-if="error" :error="error" />
    <ArticleSkeleton v-if="loading && !error" />
    <section v-if="!loading && !error" aria-label="Continue reading" class="py-8 lg:py-24 my-4">
        <div class="px-4 mx-auto max-w-screen-xl">
            <h2 class="mb-8 text-2xl font-bold text-gray-900 dark:text-white">{{ $t('articles') }}</h2>
            <div class="grid gap-12 sm:grid-cols-2 lg:grid-cols-4">
                <article
                    class="max-w-xs border border-gray-300 dark:border-gray-700 hover:border-gray-400 dark:hover:border-gray-500 rounded-lg px-2 py-2">
                    <RouterLink :to="'/post-article-1'">
                        <img src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/article/blog-1.png"
                            class="mb-5 rounded-lg" alt="Image 1">
                    </RouterLink>
                    <h2 class="mb-2 text-xl font-bold leading-tight text-gray-900 dark:text-white">
                        <RouterLink :to="'/post-article-1'">Our first office</RouterLink>
                    </h2>
                    <p class="mb-4 font-sans text-gray-500 dark:text-gray-400">Over the past year, Volosoft has undergone
                        many changes! After months of preparation.</p>
                    <RouterLink :to="'/post-article-1'"
                        class="inline-flex items-center font-semibold underline underline-offset-4 text-gray-600 dark:text-white hover:no-underline">
                        Read in 2 minutes
                    </RouterLink>
                </article>
                <article
                    class="max-w-xs border border-gray-300 dark:border-gray-700 hover:border-gray-400 dark:hover:border-gray-500 rounded-lg px-2 py-2">
                    <RouterLink :to="'/post-article-2'">
                        <img src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/article/blog-2.png"
                            class="mb-5 rounded-lg" alt="Image 2">
                    </RouterLink>
                    <h2 class="mb-2 text-xl font-bold leading-tight text-gray-900 dark:text-white">
                        <RouterLink :to="'/post-article-2'">Enterprise design tips</RouterLink>
                    </h2>
                    <p class="mb-4 font-sans text-gray-500 dark:text-gray-400">Over the past year, Volosoft has undergone
                        many changes! After months of preparation.</p>
                    <RouterLink :to="'/post-article-2'"
                        class="inline-flex items-center font-semibold underline underline-offset-4 text-gray-600 dark:text-white hover:no-underline">
                        Read in 12 minutes
                    </RouterLink>
                </article>
                <article
                    class="max-w-xs border border-gray-300 dark:border-gray-700 hover:border-gray-400 dark:hover:border-gray-500 rounded-lg px-2 py-2">
                    <RouterLink :to="'/post-article-3'">
                        <img src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/article/blog-3.png"
                            class="mb-5 rounded-lg" alt="Image 3">
                    </RouterLink>
                    <h2 class="mb-2 text-xl font-bold leading-tight text-gray-900 dark:text-white">
                        <RouterLink :to="'/post-article-3'">We partnered with Google</RouterLink>
                    </h2>
                    <p class="mb-4 font-sans text-gray-500 dark:text-gray-400">Over the past year, Volosoft has undergone
                        many changes! After months of preparation.</p>
                    <RouterLink :to="'/post-article-3'"
                        class="inline-flex items-center font-semibold underline underline-offset-4 text-gray-600 dark:text-white hover:no-underline">
                        Read in 8 minutes
                    </RouterLink>
                </article>
                <article
                    class="max-w-xs border border-gray-300 dark:border-gray-700 hover:border-gray-400 dark:hover:border-gray-500 rounded-lg px-2 py-2">
                    <RouterLink :to="'/post-article-4'">
                        <img src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/article/blog-4.png"
                            class="mb-5 rounded-lg" alt="Image 4">
                    </RouterLink>
                    <h2 class="mb-2 text-xl font-bold leading-tight text-gray-900 dark:text-white">
                        <RouterLink :to="'/post-article-4'">Our first project with React</RouterLink>
                    </h2>
                    <p class="mb-4 font-sans text-gray-500 dark:text-gray-400">Over the past year, Volosoft has undergone
                        many changes! After months of preparation.</p>
                    <RouterLink :to="'/post-article-4'"
                        class="inline-flex items-center font-semibold underline underline-offset-4 text-gray-600 dark:text-white hover:no-underline">
                        Read in 4 minutes
                    </RouterLink>
                </article>
            </div>
        </div>
        <!-- Pagination -->
        <div class="col-span-2 md:col-span-3 sm:mt-2 my-4">
            <div class="flex items-center justify-center">
                <nav aria-label="Page navigation example">
                    <ul class="inline-flex -space-x-px text-sm my-2">
                        <li>
                            <a href="#"
                                class="flex items-center mx-4 justify-center px-3 h-8 ml-0 leading-tight text-gray-500 border border-gray-300 dark:border-gray-700 hover:border-gray-400 dark:hover:border-gray-500 py-2 dark:text-gray-400 dark:hover:bg-gray-800 dark:hover:text-white rounded-lg">
                                <svg class="w-5 h-5 text-gray-800 dark:text-white" aria-hidden="true"
                                    xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 8 14">
                                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"
                                        stroke-width="1" d="M7 1 1.3 6.326a.91.91 0 0 0 0 1.348L7 13" />
                                </svg>
                            </a>
                        </li>
                        <li>
                            <a href="#"
                                class="flex items-center justify-center px-3 h-8 leading-tight text-gray-500 border border-gray-300 dark:border-gray-700 hover:border-gray-400 dark:hover:border-gray-500 py-2 dark:text-gray-400 dark:hover:bg-gray-800 dark:hover:text-white rounded-lg">
                                <svg class="w-5 h-5 text-gray-800 dark:text-white" aria-hidden="true"
                                    xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 8 14">
                                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"
                                        stroke-width="1" d="m1 13 5.7-5.326a.909.909 0 0 0 0-1.348L1 1" />
                                </svg>
                            </a>
                        </li>
                    </ul>
                </nav>
            </div>
        </div>
        <!-- Pagination -->
    </section>
</template>

<style lang="scss" scoped></style>