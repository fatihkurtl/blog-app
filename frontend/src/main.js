import "./assets/main.css";

import { createApp } from "vue";
import { createPinia } from "pinia";
import { createI18n } from "vue-i18n";
import VueValidate from 'v-validate';

import TR from "./locales/tr.json";
import EN from "./locales/en.json";

import App from "./App.vue";
import router from "./router";

import { useLangStore } from "./stores/language";

const app = createApp(App);
app.use(createPinia());

const store = useLangStore();

const i18n = createI18n({
  locale: store.locale,
  messages: {
    TR: TR,
    EN: EN,
  },
});

app.use(i18n);
app.use(router);

app.use(VueValidate);

app.mount("#app");
