<script setup>
import { ref, reactive, computed, onMounted, watch } from 'vue';
import { createAccount } from '../../composables/member/register';
import ValidationRules, { formValidation, characterLimits } from '../../validations/validation';
import { photoErrorsObject, termsErrorsObject } from '../../validations/errors/errorObjects';

const memberData = reactive({
    fullName: '',
    userName: '',
    email: '',
    password: '',
    profilePhoto: null,
});

const terms = ref(false);

const errors = ref({
    fullName: '',
    userName: '',
    email: '',
    password: '',
});

const allInputsFilled = computed(() => {
    return memberData.fullName !== '' &&
        memberData.userName !== '' &&
        memberData.email !== '' &&
        memberData.password !== '';
});

const newUser = async () => {
    if (!allInputsFilled.value) {
        for (const field in errors.value) {
            if (memberData[field] === '') {
                errors.value[field] = 'This field is required.';
                if (memberData[field]) {
                    errors.value[field] = '';
                }
            }
        }
        return;
    }
    for (const field in errors.value) {
        if (memberData[field] !== '') {
            errors.value[field] = '';
        }
    }
    // ayri bir validation'a gecirilip switch case ile yapilacak
    if (!ValidationRules.fullName.test(memberData.fullName)) {
        console.log(ValidationRules.fullName.test(memberData.fullName));
        formValidation.isFullNameValid = ValidationRules.fullName.test(memberData.fullName);
        return false;
    } else if (!ValidationRules.userName.test(memberData.userName)) {
        formValidation.isUsernameValid = ValidationRules.userName.test(memberData.userName);
        console.log('username yanlis', ValidationRules.userName.test(memberData.userName));
        return false;
    } else if (!ValidationRules.email.test(memberData.email)) {
        formValidation.isEmailValid = ValidationRules.email.test(memberData.email);
        console.log('email yanlis', ValidationRules.email.test(memberData.email));
        return false;
    } else if (!ValidationRules.password.test(memberData.password)) {
        formValidation.isPasswordValid = ValidationRules.password.test(memberData.password);
        console.log('password', ValidationRules.password.test(memberData.password));
        return false;
    } else {
        if (terms.value === true) {
            await createAccount(memberData);
            return true;
        } else {
            termsErrorsObject.isActive = true;
        }
    }
}

watch(terms, (newValue, oldValue) => {
    if (oldValue === false) {
        termsErrorsObject.isActive = false
    }
});

watch(() => memberData.fullName, (newFullName) => {
    if (newFullName) {
        formValidation.isFullNameValid = ValidationRules.fullName.test(newFullName);
    } else {
        formValidation.isFullNameValid = true;
    }
});

watch(() => memberData.userName, (newUserName) => {
    if (newUserName) {
        formValidation.isUsernameValid = ValidationRules.userName.test(newUserName);
    } else {
        formValidation.isUsernameValid = true;
    }
});

watch(() => memberData.email, (newEmail) => {
    if (newEmail) {
        formValidation.isEmailValid = ValidationRules.email.test(newEmail);
    } else {
        formValidation.isEmailValid = true;
    }
});

watch(() => memberData.password, (newPassword) => {
    if (newPassword) {
        formValidation.isPasswordValid = ValidationRules.password.test(newPassword);
    } else {
        formValidation.isPasswordValid = true;
    }
});

const uploadProfilePhoto = (e) => {
    const photo = e.target.files;
    if (!ValidationRules.profilePhoto.test(photo[0].name)) {
        photoErrorsObject.isActive = true;
        memberData.profilePhoto = null;
        return false;
    } else if (!ValidationRules.profilePhotoSize.test(photo[0].size)) {
        photoErrorsObject.isActive = true;
        memberData.profilePhoto = null;
        return false;
    } else {
        photoErrorsObject.isActive = false;
        memberData.profilePhoto = photo[0];
    }
}

</script>

<template>
    <section class="bg-white dark:bg-darkBgColor">
        <div class="py-8 px-4 mx-auto max-w-screen-xl lg:py-16 grid lg:grid-cols-2 gap-8 lg:gap-16">
            <div class="flex flex-col justify-center">
                <h1
                    class="mb-4 text-4xl font-extrabold tracking-tight leading-none text-gray-600 md:text-5xl lg:text-6xl dark:text-white">
                    {{ $t('register-banner') }}
                </h1>
                <p class="mb-6 text-lg font-sans font-normal text-gray-500 lg:text-xl dark:text-gray-400">
                    {{ $t('join-community') }}
                </p>
            </div>
            <div>
                <div class="w-full lg:max-w-xl p-6 space-y-8 sm:p-8 bg-lightItemsColor shadow-xl dark:bg-darkItemsColor">
                    <h2 class="text-gray-600 dark:text-white text-3xl font-extrabold mb-6 text-center">{{ $t('sign-up') }}
                    </h2>
                    <form method="POST" @submit.prevent="newUser" enctype="multipart/form-data">
                        <div class="mb-4">
                            <label for="fullName"
                                class="block text-gray-600 dark:text-white text-sm font-sans font-semibold mb-2"> {{
                                    $t('fullname') }}</label>
                            <input :maxlength="characterLimits.fullName" v-model="memberData.fullName"
                                v-validate="ValidationRules.fullName" type="text" id="fullName" name="fullName"
                                :placeholder="$t('fullname')"
                                class="bg-gray-50 border border-gray-300 text-gray-600 text-sm font-sans font-semibold rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-black dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                            <span v-if="errors.fullName" class="text-xs text-red-600 dark:text-red-500 font-sans">
                                <!-- {{ errors.fullName }} -->
                                {{ $t('field-is-required') }}
                            </span>
                            <p v-show="!formValidation.isFullNameValid" id="filled_error_help"
                                class="mt-2 text-xs font-sans text-red-600 dark:text-red-500">
                                <span class="font-medium">{{ $t('error') }}!</span> {{ $t('fullname-valid') }}
                            </p>
                        </div>
                        <div class="mb-4">
                            <label for="userName"
                                class="block text-gray-600 dark:text-white text-sm font-sans font-semibold mb-2">{{
                                    $t('username') }}</label>
                            <input :maxlength="characterLimits.userName" v-model="memberData.userName"
                                v-validate="ValidationRules.userName" type="text" id="userName" name="userName"
                                :placeholder="$t('username')"
                                class="bg-gray-50 border border-gray-300 text-gray-600 text-sm font-sans font-semibold rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-black dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                            <span v-if="errors.userName" class="text-xs text-red-600 dark:text-red-500 font-sans">
                                <!-- {{ errors.userName }} -->
                                {{ $t('field-is-required') }}
                            </span>
                            <p v-show="!formValidation.isUsernameValid" id="filled_error_help"
                                class="mt-2 text-xs font-sans text-red-600 dark:text-red-500">
                                <span class="font-medium">{{ $t('error') }}!</span> {{ $t('username-valid') }}
                            </p>
                        </div>
                        <div class="mb-4">
                            <label for="email"
                                class="block text-gray-600 dark:text-white text-sm font-sans font-semibold mb-2">{{
                                    $t('e-mail') }}</label>
                            <input :maxlength="characterLimits.email" v-model="memberData.email"
                                v-validate="ValidationRules.email" type="email" id="email" name="email"
                                class="bg-gray-50 border border-gray-300 text-gray-600 text-sm font-sans font-semibold rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-black dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                :placeholder="$t('e-mail')">
                            <span v-if="errors.email" class="text-xs text-red-600 dark:text-red-500 font-sans">
                                <!-- {{ errors.email }} -->
                                {{ $t('field-is-required') }}
                            </span>
                            <p v-show="!formValidation.isEmailValid" id="filled_error_help"
                                class="mt-2 text-xs font-sans text-red-600 dark:text-red-500">
                                <span class="font-medium">{{ $t('error') }}!</span> {{ $t('email-valid') }}
                            </p>
                        </div>
                        <div class="mb-4">
                            <label for="password"
                                class="block text-gray-600 dark:text-white text-sm font-sans font-semibold mb-2">{{
                                    $t('password') }}</label>
                            <input :maxlength="characterLimits.password" v-model="memberData.password"
                                v-validate="ValidationRules.password" type="password" id="password" name="password"
                                placeholder="•••••••••"
                                class="bg-gray-50 border border-gray-300 text-gray-600 text-sm font-sans font-semibold rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-black dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                            <span v-if="errors.password" class="text-xs text-red-600 dark:text-red-500 font-sans">
                                <!-- {{ errors.password }} -->
                                {{ $t('field-is-required') }}
                            </span>
                            <p v-show="!formValidation.isPasswordValid" id="filled_error_help"
                                class="mt-2 text-xs font-sans text-red-600 dark:text-red-500">
                                <span class="font-medium">{{ $t('error') }}!</span> {{ $t('password-valid') }}
                            </p>
                        </div>
                        <div class="mb-4">
                            <label for="profilePhoto"
                                class="block text-gray-600 dark:text-white text-sm font-sans font-semibold mb-2">
                                {{ $t('profile-picture') }}
                            </label>
                            <input @change="uploadProfilePhoto" accept="image/*" max-file-size="3mb" file-upload
                                class="block w-full text-sm font-sans font-semibold text-gray-600 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-black dark:border-gray-600 dark:placeholder-gray-400"
                                id="profilePhoto" type="file">
                            <p :class="[photoErrorsObject.isActive === true ? photoErrorsObject : 'mt-1 text-sm font-sans text-gray-500 dark:text-white']"
                                id="file_input_help">
                                JPEG, PNG, JPG {{ $t('or') }} SVG (MAX. 3MB).
                            </p>
                        </div>
                        <div class="mb-4 flex items-center">
                            <input type="checkbox" v-model="terms" id="terms" name="terms"
                                class="mr-2 w-4 h-4 border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-blue-300 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:bg-gray-700 dark:border-gray-600">
                            <label for="terms"
                                :class="[termsErrorsObject.isActive === true ? termsErrorsObject : 'text-sm font-sans text-gray-500 dark:text-white']">
                                <RouterLink to="/terms-and-conditions" class="underline">{{ $t('terms') }}</RouterLink>
                            </label>
                        </div>
                        <button type="submit"
                            class="w-full disabled:dark:bg-gray-500 disabled:bg-gray-500 px-5 py-3 text-base font-sans font-semibold text-center text-white bg-lightBtnColor hover:bg-sky-600 dark:bg-darkBtnColor dark:hover:bg-sky-700 rounded-lg focus:ring-4 focus:ring-blue-300 sm:w-auto dark:focus:ring-sky-800">
                            {{ $t('register') }}
                        </button>
                        <div class="mt-4 text-sm font-sans font-medium flex items-end text-gray-500 dark:text-white">
                            {{ $t('already-member') }}
                            <RouterLink to="/login" class="font-sans text-blue-600 hover:underline dark:text-blue-500">
                                {{ $t('login') }}
                            </RouterLink>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </section>
</template>

<style lang="scss" scoped></style>