<script setup>

</script>

<template>
    <section aria-label="Continue reading" class="py-8 lg:py-24 my-4">
        <div class="px-4 mx-auto max-w-screen-xl">
            <h2 class="mb-8 text-2xl font-bold text-gray-900 dark:text-white">{{ $t('continue-reading') }}</h2>
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
    </section>
</template>

<style lang="scss" scoped></style>