/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
    "./node_modules/flowbite/**/*.js",
  ],
  theme: {
    extend: {
      colors: {
        darkBgColor: {
          DEFAULT: "#000000", //#2F3031
        },
        darkItemsColor: {
          DEFAULT: "#18191a",
        },
        darkBtnColor: {
          DEFAULT: "#0284c7",
        },
        borderColor: {
          DEFAULT: "#393a3b",
        },
        lightBgColor: {
          DEFAULT: "#fff",
        },
        lightItemsColor: {
          DEFAULT: "#f8f9fa" // #F0F0F0
        },
        lightBtnColor: {
          DEFAULT: "#0369a1",
        },
      },
    },
  },
  plugins: [require("flowbite/plugin")],
};
