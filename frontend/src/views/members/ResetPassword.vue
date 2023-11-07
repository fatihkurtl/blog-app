<script setup>
import { ref, reactive, computed, onMounted, watch } from 'vue';
import ValidationRules, { formValidation } from '../../validations/validation';
import { photoErrorsObject, termsErrorsObject } from '../../validations/errors/errorObjects';
import { sendMeEmail } from '../../composables/member/sendMail';


const memberEmail = ref();

const errors = ref({
    email: '',
});

const allInputsFilled = computed(() => {
    return memberEmail.value !== ''
});

const resetLink = async () => {
    if (!allInputsFilled.value) {
        for (const field in errors.value) {
            if (memberEmail[field] === '') {
                errors.value[field] = 'This field is required.';
                if (memberEmail[field]) {
                    errors.value[field] = '';
                }
            }
        }
        return;
    }
    for (const field in errors.value) {
        if (memberEmail[field] !== '') {
            errors.value[field] = '';
        }
    }

    if (!ValidationRules.email.test(memberEmail.value)) {
        console.log('email hatali');
        formValidation.isEmailValid = ValidationRules.email.test(memberEmail.value);
    } else {
        await sendMeEmail(memberEmail.value);
    }
}

watch(() => memberEmail.value, (newEmail) => {
    if (newEmail) {
        formValidation.isEmailValid = ValidationRules.email.test(newEmail);
    } else {
        formValidation.isEmailValid = true;
    }
});

</script>

<template>
    <section class="bg-white dark:bg-darkBgColor">
        <div class="py-8 px-4 mx-auto max-w-screen-xl lg:py-16 grid lg:grid-cols-2 gap-8 lg:gap-16">
            <div class="flex flex-col justify-center">
                <h1
                    class="mb-4 text-4xl font-sans font-extrabold tracking-tight leading-none text-gray-600 md:text-5xl lg:text-6xl dark:text-white">
                    {{ $t('reset-password-banner') }}
                </h1>
            </div>
            <div>
                <div class="w-full lg:max-w-xl p-6 space-y-8 sm:p-8 lightItemsColor shadow-xl dark:bg-darkItemsColor">
                    <h2 class="text-2xl font-bold text-gray-600 dark:text-white">
                        {{ $t('reset-your-password') }}
                    </h2>
                    <form method="POST" @submit.prevent="resetLink" class="mt-8 space-y-6" enctype="multipart/form-data">
                        <div>
                            <label for="email"
                                class="block text-gray-600 dark:text-white text-sm font-sans font-semibold mb-2">
                                {{ $t('e-mail') }}
                            </label>
                            <input type="email" name="email" id="email" v-model="memberEmail"
                                class="bg-gray-50 border border-gray-300 text-gray-600 text-sm font-sans font-semibold rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                :placeholder="$t('e-mail-placeholder') + '@gmail.com'">
                            <span v-if="errors.email" class="text-xs text-red-600 dark:text-red-500 font-sans">
                                <!-- {{ errors.fullName }} -->
                                {{ $t('field-is-required') }}
                            </span>
                            <p v-show="!formValidation.isEmailValid" id="filled_error_help"
                                class="mt-2 text-xs font-sans text-red-600 dark:text-red-500">
                                <span class="font-medium">{{ $t('error') }}!</span> {{ $t('email-valid') }}
                            </p>
                        </div>
                        <button type="submit"
                            class="w-full px-5 py-3 text-base font-sans font-semibold text-center text-white bg-lightBtnColor hover:bg-sky-600 dark:hover:bg-sky-700 rounded-lg focus:ring-4 focus:ring-blue-300 sm:w-auto dark:bg-darkBtnColor dark:focus:ring-sky-800">
                            {{ $t('send-reset-link') }}
                        </button>
                    </form>
                </div>
            </div>
        </div>
    </section>
</template>

<style lang="scss" scoped></style>