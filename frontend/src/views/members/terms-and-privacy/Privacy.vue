<script setup>

</script>

<template>
    <section class="mx-auto my-4 p-8 bg-lightItemsColor dark:bg-darkItemsColor">
        <h1 class="text-gray-900 dark:text-white text-3xl font-extrabold mb-6 text-center">{{ $t('privacy-header') }}</h1>
        <p class="block text-gray-600 dark:text-white text-md font-sans font-semibold mb-4">
            {{ $t('privacy-description') }}
        </p>
        <div class="list-decimal pl-8 mb-4">
            <p class="block text-gray-600 dark:text-white text-md font-sans font-semibold mb-2">1. {{ $t('privacy-rule-1')
            }}
            </p>
            <p class="block text-gray-600 dark:text-white text-md font-sans font-semibold mb-2">2. {{ $t('privacy-rule-2')
            }}
            </p>
            <p class="block text-gray-600 dark:text-white text-md font-sans font-semibold mb-2">3. {{ $t('privacy-rule-3')
            }}
            </p>
            <p class="block text-gray-600 dark:text-white text-md font-sans font-semibold mb-2">4. {{ $t('privacy-rule-4')
            }}
            </p>
            <p class="block text-gray-600 dark:text-white text-md font-sans font-semibold mb-2">5. {{ $t('privacy-rule-5')
            }}
            </p>
            <p class="block text-gray-600 dark:text-white text-md font-sans font-semibold mb-2">6. {{ $t('privacy-rule-6')
            }}
            </p>
            <p class="block text-gray-600 dark:text-white text-md font-sans font-semibold mb-2">7. {{ $t('privacy-rule-7')
            }}
            </p>
            <p class="block text-gray-600 dark:text-white text-md font-sans font-semibold mb-2">8. {{ $t('privacy-rule-8')
            }}
                <RouterLink to="/contact" class="font-sans text-sm text-blue-600 hover:underline dark:text-blue-500">
                    {{ $t('click-here') }}
                </RouterLink>
                .
            </p>
        </div>
        <p class="block text-gray-600 dark:text-white text-md font-sans font-semibold mb-2">{{ $t('privacy-footer') }}</p>
    <p class="text-sm text-gray-500 dark:text-white font-sans">{{ $t('privacy-last-update') }}: 29.01.2023</p>
</section></template>


<style lang="scss" scoped></style>