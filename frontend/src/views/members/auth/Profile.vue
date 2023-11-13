<script setup>
import { useRouter } from 'vue-router';

const router = useRouter();
</script>

<template>
    <main class="container mx-auto mt-4 mb-4 lg:px-0 flex justify-center items-center">
        <section class="bg-lightItemsColor dark:bg-darkItemsColor col-span-3 max-w-3xl min-w-full lg:min-w-full">
            <div class="container mx-auto px-4 py-8">
                <div class="flex flex-col md:flex-row items-center justify-between">
                    <div class="w-full md:w-1/3">
                        <img class="rounded-full w-48 h-48 mx-auto" src="/src/assets/images/visitor.png" alt="Fatih Kurt">
                        <h1 class="text-4xl text-gray-600 dark:text-white font-sans font-bold text-center mt-4">Fatih Kurt
                        </h1>
                        <p class="text-md font-sans text-gray-600 dark:text-gray-400 text-center">Fullstack Developer</p>
                        <p class="text-md font-sans text-gray-600 dark:text-gray-400 text-center">
                            {{ $t('joined-on') }} Oct 13, 2023
                        </p>
                        <div class="flex justify-center mt-4 space-x-4">
                            <div class="text-gray-600 dark:text-gray-400 font-sans font-semibold">Turkey, Bursa</div>
                            <!-- <a href="#" class="text-blue-500 font-sans font-semibold hover:underline">X</a>
                            <a href="#" class="text-blue-500 font-sans font-semibold hover:underline">GitHub</a>
                            <a href="#" class="text-blue-500 font-sans font-semibold hover:underline">LinkedIn</a> -->
                        </div>
                        <div class="flex justify-center mt-4 space-x-4">
                            <!-- <div class="text-gray-600 dark:text-gray-400 font-sans font-semibold">Turkey, Bursa</div> -->
                            <a href="#" class="text-blue-500 font-sans font-semibold hover:underline">X</a>
                            <a href="#" class="text-blue-500 font-sans font-semibold hover:underline">GitHub</a>
                            <a href="#" class="text-blue-500 font-sans font-semibold hover:underline">LinkedIn</a>
                        </div>
                        <button @click="router.push('/settings/profile/member=:member-token')"
                            class="bg-lightBtnColor hover:bg-sky-600 dark:hover:bg-sky-700 focus:ring-4 dark:bg-darkBtnColor dark:focus:ring-sky-800 focus:ring-blue-300 font-sans text-white px-4 py-2 rounded mt-4 mx-auto block">
                            {{ $t('edit-profile') }}
                        </button>
                    </div>
                    <div class="w-full md:w-2/3 mt-8 md:mt-0 md:pl-8">
                        <h2 class="text-3xl font-bold mb-4 text-gray-600 dark:text-white">{{ $t('recent-commnets') }}</h2>
                        <p class="text-lg flex items-center text-gray-600 dark:text-gray-400 mb-4">
                            <!-- <svg class="w-6 h-6 text-gray-600 dark:text-gray-400" aria-hidden="true"
                                xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 18">
                                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1"
                                    d="M5 5h5M5 8h2m6-3h2m-5 3h6m2-7H2a1 1 0 0 0-1 1v9a1 1 0 0 0 1 1h3v5l5-5h8a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1Z" />
                            </svg> -->
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                stroke="currentColor" class="w-6 h-6 text-gray-600 dark:text-gray-400">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M12 20.25c4.97 0 9-3.694 9-8.25s-4.03-8.25-9-8.25S3 7.444 3 12c0 2.104.859 4.023 2.273 5.48.432.447.74 1.04.586 1.641a4.483 4.483 0 01-.923 1.785A5.969 5.969 0 006 21c1.282 0 2.47-.402 3.445-1.087.81.22 1.668.337 2.555.337z" />
                            </svg>

                        <blockquote class="ml-2"> 12 </blockquote>
                        <blockquote class="ml-2">{{ $t('comment-written') }}</blockquote>
                        </p>
                        <div class="space-y-4">
                            <div class="flex items-start">
                                <img class="rounded-full w-12 h-12 mr-4" src="https://via.placeholder.com/400x300"
                                    alt="Article 1">
                                <div class="flex flex-col">
                                    <a href="#" class="text-xl text-blue-500 hover:underline">How to use Tailwind CSS with
                                        Next.js</a>
                                    <p class="text-lg text-gray-800 dark:text-white mt-2">Great article! I learned a lot
                                        from your examples.
                                        Thanks for sharing!</p>
                                    <p class="text-sm text-gray-600 dark:text-white mt-2">2 {{ $t('hours-ago') }}</p>
                                </div>
                            </div>
                            <div class="flex items-start">
                                <img class="rounded-full w-12 h-12 mr-4" src="https://via.placeholder.com/400x300"
                                    alt="Article 2">
                                <div class="flex flex-col">
                                    <a href="#" class="text-xl text-blue-500 hover:underline">10 tips to improve your coding
                                        skills</a>
                                    <p class="text-lg text-gray-800 dark:text-white mt-2">Very useful tips! I especially
                                        liked the one about
                                        reading other people's code. I think it's a great way to learn new techniques and
                                        best practices.</p>
                                    <p class="text-sm text-gray-600 dark:text-white mt-2">1 {{ $t('day-ago') }}</p>
                                </div>
                            </div>
                            <div class="flex items-start">
                                <img class="rounded-full w-12 h-12 mr-4" src="https://via.placeholder.com/400x300"
                                    alt="Article 3">
                                <div class="flex flex-col">
                                    <a href="#" class="text-xl text-blue-500 hover:underline">Why I love CodeSandbox</a>
                                    <p class="text-lg text-gray-800 dark:text-white mt-2">CodeSandbox is awesome! I use it
                                        all the time for
                                        prototyping and testing ideas. It's so easy and fast to set up and deploy. Kudos to
                                        you and your team for creating such a wonderful tool!</p>
                                    <p class="text-sm text-gray-600 dark:text-white mt-2">2 {{ $t('days-ago') }}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </main>
</template>

<style lang="scss" scoped></style>