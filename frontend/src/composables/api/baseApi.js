export const baseApi = () => {
    return 'http://127.0.0.1:8000' || import.meta.env.VITE_API_BASE_URL;
}