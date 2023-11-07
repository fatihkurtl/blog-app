<script setup>
import { ref, reactive, computed, watch } from 'vue';
import { sendNewPassword } from '../../../composables/member/newPassword';
import ValidationRules, { formValidation, characterLimits } from '../../../validations/validation';


const newPassword = reactive({
    password: '',
    confirmPassword: '',
});

const errors = ref({
    password: '',
    confirmPassword: '',
});

const isPasswordsSame = ref(true);

const allInputsFilled = computed(() => {
    return newPassword.password !== '' &&
        newPassword.confirmPassword !== '';
});

const saveNewPassword = async () => {
    if (!allInputsFilled.value) {
        for (const field in errors.value) {
            if (newPassword[field] === '') {
                errors.value[field] = 'This field is required.';
                if (newPassword[field]) {
                    errors.value[field] = '';
                }
            }
        }
        return;
    }
    for (const field in errors.value) {
        if (newPassword[field] !== '') {
            errors.value[field] = '';
        }
    }

    if (!ValidationRules.password.test(newPassword.password)) {
        formValidation.isPasswordValid = ValidationRules.password.test(newPassword.password);
        return false;
    } else if (!ValidationRules.password.test(newPassword.confirmPassword)) {
        formValidation.isConfirmPasswordValid = ValidationRules.password.test(newPassword.confirmPassword);
        return false;
    } else if (newPassword.password === newPassword.confirmPassword) {
        await sendNewPassword(newPassword.password);
    }
    else {
        isPasswordsSame.value = false;
    }
}

watch(() => newPassword.password, (newpassword) => {
    if (newpassword) {
        formValidation.isPasswordValid = ValidationRules.password.test(newpassword);
    } else {
        formValidation.isPasswordValid = true;
    }
});

watch(() => newPassword.confirmPassword, (newConfirmPassword) => {
    if (newConfirmPassword) {
        formValidation.isConfirmPasswordValid = ValidationRules.password.test(newConfirmPassword);
    } else {
        formValidation.isConfirmPasswordValid = true;
    }
});

watch(newPassword, (newValue) => {
    if (newValue.confirmPassword) {
        if (newValue.password !== newValue.confirmPassword) {
            isPasswordsSame.value = false;
        } else {
            isPasswordsSame.value = true;
        }
    } else {
        isPasswordsSame.value = true;
    }
})

</script>

<template>
    <section class="bg-white dark:bg-darkBgColor">
        <div class="py-8 px-4 mx-auto max-w-screen-xl lg:py-16 grid lg:grid-cols-2 gap-8 lg:gap-16">
            <div class="flex flex-col justify-center">
                <h1
                    class="mb-4 text-4xl font-extrabold tracking-tight leading-none text-gray-600 md:text-5xl lg:text-6xl dark:text-white">
                    {{ $t('new-password-banner') }}</h1>
                <p class="mb-6 text-lg font-sans font-normal text-gray-500 lg:text-xl dark:text-gray-400">
                    {{ $t('new-password-info') }}
                </p>
            </div>
            <div>
                <div class="w-full lg:max-w-xl p-6 space-y-8 sm:p-8 bg-lightItemsColor shadow-xl dark:bg-darkItemsColor">
                    <h2 class="text-2xl font-bold text-gray-600 dark:text-white">
                        {{ $t('new-password') }}
                    </h2>
                    <form class="mt-8 space-y-6" method="POST" @submit.prevent="saveNewPassword"
                        enctype="multipart/form-data">
                        <div>
                            <label for="password"
                                class="block text-gray-600 dark:text-white text-sm font-sans font-semibold mb-2">{{
                                    $t('password') }}</label>
                            <input :maxlength="characterLimits.password" v-model="newPassword.password" type="password"
                                name="password" id="password" placeholder="••••••••"
                                class="bg-gray-50 border border-gray-300 text-gray-600 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                            <span v-if="errors.password" class="text-xs text-red-600 dark:text-red-500 font-sans">
                                <!-- {{ errors.password }} -->
                                {{ $t('field-is-required') }}
                            </span>
                            <p v-show="!formValidation.isPasswordValid" id="filled_error_help"
                                class="mt-2 text-xs font-sans text-red-600 dark:text-red-500">
                                <span class="font-medium">{{ $t('error') }}!</span> {{ $t('password-valid') }}
                            </p>
                            <p v-show="!isPasswordsSame" id="filled_error_help"
                                class="mt-2 text-xs font-sans text-red-600 dark:text-red-500">
                                <span class="font-medium">{{ $t('error') }}!</span> {{ $t('is-passwords-same') }}
                            </p>
                        </div>
                        <div>
                            <label for="confirm-password"
                                class="block text-gray-600 dark:text-white text-sm font-sans font-semibold mb-2">{{
                                    $t('confirm-password') }}</label>
                            <input :maxlength="characterLimits.password" v-model="newPassword.confirmPassword"
                                type="password" name="confirm-password" id="confirm-password" placeholder="••••••••"
                                class="bg-gray-50 border border-gray-300 text-gray-600 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                            <span v-if="errors.confirmPassword" class="text-xs text-red-600 dark:text-red-500 font-sans">
                                <!-- {{ errors.password }} -->
                                {{ $t('field-is-required') }}
                            </span>
                            <p v-show="!formValidation.isConfirmPasswordValid" id="filled_error_help"
                                class="mt-2 text-xs font-sans text-red-600 dark:text-red-500">
                                <span class="font-medium">{{ $t('error') }}!</span> {{ $t('password-valid') }}
                            </p>
                            <p v-show="!isPasswordsSame" id="filled_error_help"
                                class="mt-2 text-xs font-sans text-red-600 dark:text-red-500">
                                <span class="font-medium">{{ $t('error') }}!</span> {{ $t('is-passwords-same') }}
                            </p>
                        </div>
                        <button type="submit"
                            class="w-full px-5 py-3 text-base font-sans font-semibold text-center text-white bg-lightBtnColor hover:bg-sky-600 dark:hover:bg-sky-700 rounded-lg focus:ring-4 focus:ring-blue-300 sm:w-auto dark:bg-darkBtnColor dark:focus:ring-sky-800">
                            {{ $t('save') }}
                        </button>
                    </form>
                </div>
            </div>
        </div>
    </section>
</template>

<style lang="scss" scoped></style>