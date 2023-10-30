<script setup>
const show = defineProps(['showCommentSuccess']);

</script>

<template>
    <div v-if="show.showCommentSuccess" class="bg-green-100 dark:bg-green-100 border-l-4 border-green-500 dark:border-green-500 text-green-800 dark:text-green-800 p-4 animate-fade-in" role="alert">
        <div class="flex items-center">
            <svg class="w-6 h-6 mr-2 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
            </svg>
            <p>
                {{$t('comment-success')}}
            </p>
        </div>
    </div>
</template>

<style lang="css" scoped>
@keyframes fade-in {
    0% {
        opacity: 0;
    }

    100% {
        opacity: 1;
    }
}

@keyframes fade-out {
    0% {
        opacity: 1;
    }

    100% {
        opacity: 0;
    }
}

.animate-fade-in {
    animation: fade-in 1s ease-out;
}

.animate-fade-out {
    animation: fade-out 1s ease-in;
}
</style>