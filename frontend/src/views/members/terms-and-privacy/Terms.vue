<script setup>

</script>

<template>
    <section class="mx-auto my-4 p-8 bg-lightItemsColor dark:bg-darkItemsColor">
        <h1 class="text-gray-600 dark:text-white text-3xl font-extrabold mb-6 text-center">{{ $t('terms-header') }}</h1>
        <p class="block text-gray-600 dark:text-white text-md font-sans font-semibold mb-4">
            {{ $t('terms-description') }}
        </p>
        <div class="list-decimal pl-8 mb-4">
            <p class="block text-gray-600 dark:text-white text-md font-sans font-semibold mb-2">1. {{ $t('terms-rule-1') }}
            </p>
            <p class="block text-gray-600 dark:text-white text-md font-sans font-semibold mb-2">2. {{ $t('terms-rule-2') }}
            </p>
            <p class="block text-gray-600 dark:text-white text-md font-sans font-semibold mb-2">3. {{ $t('terms-rule-3') }}
            </p>
            <p class="block text-gray-600 dark:text-white text-md font-sans font-semibold mb-2">4. {{ $t('terms-rule-4') }}
            </p>
            <p class="block text-gray-600 dark:text-white text-md font-sans font-semibold mb-2">5. {{ $t('terms-rule-5') }}
            </p>
            <p class="block text-gray-600 dark:text-white text-md font-sans font-semibold mb-2">6. {{ $t('terms-rule-6') }}
            </p>
            <p class="block text-gray-600 dark:text-white text-md font-sans font-semibold mb-2">7. {{ $t('terms-rule-7') }}
            </p>
            <p class="block text-gray-600 dark:text-white text-md font-sans font-semibold mb-2">8. {{ $t('terms-rule-8') }}
            </p>
            <p class="block text-gray-600 dark:text-white text-md font-sans font-semibold mb-2">9. {{ $t('terms-rule-9') }}
            </p>
            <p class="block text-gray-600 dark:text-white text-md font-sans font-semibold mb-2">10. {{ $t('terms-rule-10')
            }}
            </p>
            <p class="block text-gray-600 dark:text-white text-md font-sans font-semibold mb-2">11. {{ $t('terms-rule-11')
            }}
                <RouterLink to="/contact" class="font-sans text-sm text-blue-600 hover:underline dark:text-blue-500">
                    {{ $t('click-here') }}
                </RouterLink>
                .
            </p>
            <p class="block text-gray-600 dark:text-white text-md font-sans font-semibold mb-2">12. {{ $t('terms-rule-12')
            }} <a href="mailto:support@fullstack.com"
                    class="font-sans text-sm text-blue-600 hover:underline dark:text-blue-500">support@fullstack.com</a>.
            </p>

        </div>
        <p class="block text-gray-600 dark:text-white text-md font-sans font-semibold mb-2">{{ $t('terms-footer') }}</p>
        <p class="text-sm text-gray-500 dark:text-white font-sans">{{ $t('terms-last-update') }}: 29.01.2023</p>
    </section>
</template>


<style lang="scss" scoped></style>