import { ref, onMounted } from "vue";
import { defineStore } from "pinia";

export const useLangStore = defineStore("locale", () => {
  const locale = ref(localStorage.getItem("lang") || "TR");

  function setLang(lang) {
    localStorage.setItem("lang", lang);
    locale.value = lang;
    window.location.reload();
  }

  function langCheck() {
    const storedLang = localStorage.getItem("lang");
    if (storedLang) {
      locale.value = storedLang;
    }
  }
  langCheck();

  return { locale, setLang };
});
