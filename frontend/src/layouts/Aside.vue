<script setup>

</script>

<template>
    <aside class="col-span-1 hidden sm:block">
        <div class="bg-lightItemsColor dark:bg-darkItemsColor p-4">

            <h3 class="text-xl font-sans font-bold text-black dark:text-white mb-4">{{ $t('latest-posts') }}</h3>
            <ul>
                <li class="py-3 sm:py-4 mb-2">
                    <RouterLink to="/post-detail-1" class="flex items-center">
                        <div class="flex-shrink-0">
                            <img class="w-8 h-8 rounded-full" src="https://via.placeholder.com/400x300" alt="Neil image">
                        </div>
                        <div class="flex-1 min-w-0 ms-4">
                            <p class="text-md font-sans font-semibold hover:text-blue-500 dark:hover:text-blue-500 text-gray-600 truncate dark:text-white">
                                Blog Post 1
                            </p>
                            <p class="text-sm text-gray-500 truncate dark:text-gray-400">
                                Lorem ipsum dolor sit amet, consectetur adipiscing
                                elit. Vivamus quis porta dui. Ut eu iaculis massa.
                            </p>
                        </div>
                    </RouterLink>
                </li>
                <li class="py-3 sm:py-4 mb-2">
                    <RouterLink to="/post-detail-2" class="flex items-center">
                        <div class="flex-shrink-0">
                            <img class="w-8 h-8 rounded-full" src="https://via.placeholder.com/400x300" alt="Neil image">
                        </div>
                        <div class="flex-1 min-w-0 ms-4">
                            <p class="text-md font-sans font-semibold hover:text-blue-500 dark:hover:text-blue-500 text-gray-600 truncate dark:text-white">
                                Blog Post 2
                            </p>
                            <p class="text-sm text-gray-500 truncate dark:text-gray-400">
                                Lorem ipsum dolor sit amet, consectetur adipiscing
                                elit. Vivamus quis porta dui. Ut eu iaculis massa.
                            </p>
                        </div>
                    </RouterLink>
                </li>
                <li class="py-3 sm:py-4 mb-2">
                    <RouterLink to="/post-detail-3" class="flex items-center">
                        <div class="flex-shrink-0">
                            <img class="w-8 h-8 rounded-full" src="https://via.placeholder.com/400x300" alt="Neil image">
                        </div>
                        <div class="flex-1 min-w-0 ms-4">
                            <p class="text-md font-sans font-semibold hover:text-blue-500 dark:hover:text-blue-500 text-gray-600 truncate dark:text-white">
                                Blog Post 3
                            </p>
                            <p class="text-sm text-gray-500 truncate dark:text-gray-400">
                                Lorem ipsum dolor sit amet, consectetur adipiscing
                                elit. Vivamus quis porta dui. Ut eu iaculis massa.
                            </p>
                        </div>
                    </RouterLink>
                </li>
                <!-- Daha fazla post eklemek için liste öğelerini çoğaltabilirsiniz -->
            </ul>
            <hr class="w-full h-1 my-8 bg-gray-200 border-0 dark:bg-darkBgColor">
            <h3 class="text-xl font-sans font-bold text-black dark:text-white mb-4">{{ $t('trends') }}</h3>
            <ul>
                <li class="py-3 sm:py-4 mb-2">
                    <RouterLink to="/trends/post-detail-1" class="flex items-center">
                        <div class="flex-shrink-0">
                            <img class="w-8 h-8 rounded-full" src="https://via.placeholder.com/400x300" alt="Neil image">
                        </div>
                        <div class="flex-1 min-w-0 ms-4">
                            <p class="text-md font-sans font-semibold hover:text-blue-500 dark:hover:text-blue-500 text-gray-600 truncate dark:text-white">
                                Blog Post 1
                            </p>
                            <p class="text-sm text-gray-500 truncate dark:text-gray-400">
                                Lorem ipsum dolor sit amet, consectetur adipiscing
                                elit. Vivamus quis porta dui. Ut eu iaculis massa.
                            </p>
                        </div>
                    </RouterLink>
                </li>
                <li class="py-3 sm:py-4 mb-2">
                    <RouterLink to="/trends/post-detail-2" class="flex items-center">
                        <div class="flex-shrink-0">
                            <img class="w-8 h-8 rounded-full" src="https://via.placeholder.com/400x300" alt="Neil image">
                        </div>
                        <div class="flex-1 min-w-0 ms-4">
                            <p class="text-md font-sans font-semibold hover:text-blue-500 dark:hover:text-blue-500 text-gray-600 truncate dark:text-white">
                                Blog Post 2
                            </p>
                            <p class="text-sm text-gray-500 truncate dark:text-gray-400">
                                Lorem ipsum dolor sit amet, consectetur adipiscing
                                elit. Vivamus quis porta dui. Ut eu iaculis massa.
                            </p>
                        </div>
                    </RouterLink>
                </li>
                <li class="py-3 sm:py-4 mb-2">
                    <RouterLink to="/trends/post-detail-3" class="flex items-center">
                        <div class="flex-shrink-0">
                            <img class="w-8 h-8 rounded-full" src="https://via.placeholder.com/400x300" alt="Neil image">
                        </div>
                        <div class="flex-1 min-w-0 ms-4">
                            <p class="text-md font-sans font-semibold hover:text-blue-500 dark:hover:text-blue-500 text-gray-600 truncate dark:text-white">
                                Blog Post 3
                            </p>
                            <p class="text-sm text-gray-500 truncate dark:text-gray-400">
                                Lorem ipsum dolor sit amet, consectetur adipiscing
                                elit. Vivamus quis porta dui. Ut eu iaculis massa.
                            </p>
                        </div>
                    </RouterLink>
                </li>
                <!-- Daha fazla post eklemek için liste öğelerini çoğaltabilirsiniz -->
            </ul>
        </div>
        <br />
        <!-- Contact -->
        <!-- <div class="py-8 lg:py-16 px-4 mx-auto max-w-screen-md dark:bg-darkItemsColor">
            <h2 class="mb-4 text-4xl tracking-tight font-extrabold text-center text-gray-900 dark:text-white">
                Bize Ulaşın
            </h2>
            <p class="mb-8 lg:mb-16 font-light text-center text-gray-500 dark:text-gray-400 sm:text-xl">
                Teknik bir sorununuz mu var? Bir beta özelliği hakkında geri bildirim göndermek mi istiyorsunuz? İş
                planımız hakkında ayrıntılara mı ihtiyacınız var? Bize bildirin.
            </p>
            <form action="#" class="space-y-8">
                <div>
                    <label for="email" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Email</label>
                    <input type="email" id="email"
                        class="shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500 dark:shadow-sm-light"
                        placeholder="name@gmail.com" required>
                </div>
                <div>
                    <label for="subject" class="block mb-2 text-sm font-medium text-white dark:text-gray-300">Konu</label>
                    <input type="text" id="subject"
                        class="block p-3 w-full text-sm text-white bg-gray-50 rounded-lg border border-gray-300 shadow-sm focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500 dark:shadow-sm-light"
                        placeholder="Size nasıl yardımcı olabileceğimizi bize bildirin" required>
                </div>
                <div class="sm:col-span-2">
                    <label for="message"
                        class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Mesajınız</label>
                    <textarea id="message" rows="6"
                        class="block resize-none p-2.5 w-full text-sm text-white bg-gray-50 rounded-lg shadow-sm border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                        placeholder="Yorum bırakın..."></textarea>
                </div>
                <button type="submit"
                    class="py-3 px-5 text-sm font-medium text-center text-white rounded-lg bg-primary-700 sm:w-fit hover:bg-sky-800 focus:ring-4 focus:outline-none focus:ring-primary-300 dark:bg-darkBtnColor dark:hover:bg-sky-700 dark:focus:ring-sky-800">Mesaj
                    Gönder</button>
            </form>
        </div> -->
        <!-- Contact -->
    </aside>
</template>

<style lang="scss" scoped></style>
