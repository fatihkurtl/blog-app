<script setup>

</script>

<template>
    <main class="container mx-auto mt-4 mb-4 lg:px-0 flex justify-center items-center">
        <section class="bg-lightItemsColor dark:bg-darkItemsColor col-span-3 max-w-3xl">
            <div class="container mx-auto px-4 py-8">
                <div class="flex flex-col md:flex-row items-center justify-between">
                    <div class="w-full md:w-1/3">
                        <img class="rounded-full w-48 h-48 mx-auto" src="/src/assets/images/visitor.png" alt="Fatih Kurt">
                        <h1 class="text-4xl text-gray-600 dark:text-white font-sans font-bold text-center mt-4">Fatih Kurt
                        </h1>
                        <p class="text-md font-sans text-gray-600 dark:text-gray-400 text-center">Fullstack Developer</p>
                        <div class="flex justify-center mt-4 space-x-4">
                            <div class="text-gray-600 dark:text-gray-400 font-sans font-semibold">Turkey, Bursa</div>
                            <!-- <a href="#" class="text-blue-500 font-sans font-semibold hover:underline">GitHub</a>
                            <a href="#" class="text-blue-500 font-sans font-semibold hover:underline">LinkedIn</a> -->
                        </div>
                        <button to="/settings/profile/member=:member-token"
                            class="bg-lightBtnColor hover:bg-sky-600 dark:hover:bg-sky-700 focus:ring-4 dark:bg-darkBtnColor dark:focus:ring-sky-800 focus:ring-blue-300 font-sans text-white px-4 py-2 rounded mt-4 mx-auto block">
                            {{$t('edit-profile')}}
                        </button>
                    </div>
                    <div class="w-full md:w-2/3 mt-8 md:mt-0 md:pl-8">
                        <h2 class="text-3xl font-bold mb-4 text-gray-600 dark:text-white">Comments</h2>
                        <p class="text-lg text-gray-600 dark:text-white mb-4">You have made <strong>12 comments</strong> on
                            fullstack. Here are
                            your latest comments:</p>
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
                                    <p class="text-sm text-gray-600 dark:text-white mt-2">2 hours ago</p>
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
                                    <p class="text-sm text-gray-600 dark:text-white mt-2">1 day ago</p>
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
                                    <p class="text-sm text-gray-600 dark:text-white mt-2">2 days ago</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- <figure class="p-8 bg-lightItemsColor dark:bg-darkItemsColor">
            <img class="w-24 h-24 rounded-full mx-auto" src="/src/assets/images/visitor.png" alt="" width="384" height="512">
            <div class="pt-6 text-center space-y-4">
                <figcaption class="font-semibold">
                    <div class="text-gray-600 dark:text-white text-2xl font-sans">
                        John Doe
                    </div>
                    <div class="text-gray-700 dark:text-gray-500 font-sans">
                        Fullstack Developer, TR
                    </div>
                </figcaption>
                <blockquote>
                    <p class="text-lg font-medium">
                        “Tailwind CSS is the only framework that I've seen scale
                        on large teams. It’s easy to customize, adapts to any design,
                        and the build size is tiny.”
                    </p>
                </blockquote>                        
            </div>
        </figure> -->
    </section>
</main></template>

<style lang="scss" scoped></style>