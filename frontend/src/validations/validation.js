import { reactive } from "vue";

export default class ValidationRules {
    static fullName = /^[a-zA-Z]+(?: [a-zA-Z]+)*(?: [a-zA-Z]+)?$/;
    static userName = /^[a-zA-Z0-9]+$/;
    static email = /^[a-zA-Z0-9.!#$%&'*+-/=?^_`{|}~]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    static password = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[-.])[a-zA-Z0-9-.]{8,50}$/;
    static profilePhoto = /^[a-zA-Z0-9_\-]+\.(jpg|jpeg|png|svg)$/;
    static profilePhotoSize = /(?:;?\s*size=([0-9]+))?/;
}

export const formValidation = reactive({
    isFullNameValid: true,
    isUsernameValid: true,
    isEmailValid: true,
    isPasswordValid: true,
    isConfirmPasswordValid: true,
})

export const characterLimits = reactive({
    fullName: 60,
    userName: 20,
    password: 50,
})