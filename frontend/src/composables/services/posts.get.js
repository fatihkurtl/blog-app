import { ref } from "vue";

export function useFetch(path) {
  const response = ref();
  const loading = ref(true);
  const error = ref();

  fetch(`https://dummyjson.com${path}`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((response) => response.json())
    .then((jsonData) => {
      setTimeout(() => {
        response.value = jsonData;
        loading.value = false;
      }, 1000);
    })
    .catch((e) => (error.value = e));

  return {
    response,
    loading,
    error,
  };
}
