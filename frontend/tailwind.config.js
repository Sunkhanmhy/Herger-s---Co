/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./*.html",
    "./company/*.html",
    "./practices/*.html",
    "./src/ts/**/*.ts"
  ],
  theme: {
    extend: {
      colors: {
        navy: {
          DEFAULT: "#0a1f44",
          50: "#eef1f7",
          100: "#d6ddec",
          200: "#adbbd9",
          300: "#8399c6",
          400: "#5a77b3",
          500: "#3a5a9a",
          600: "#1f3d76",
          700: "#132a56",
          800: "#0a1f44",
          900: "#061633",
          950: "#030d1f"
        },
        gold: {
          DEFAULT: "#b8860b",
          50: "#fbf3e0",
          100: "#f4e2b8",
          200: "#eccd8a",
          300: "#e3b75c",
          400: "#daa63b",
          500: "#cf9720",
          600: "#b8860b",
          700: "#916909",
          800: "#6c4e07",
          900: "#493505",
          950: "#2c2003"
        }
      },
      fontFamily: {
        serif: ["'Playfair Display'", "Georgia", "serif"],
        sans: ["'Inter'", "system-ui", "sans-serif"]
      },
      boxShadow: {
        glass: "0 8px 32px 0 rgba(10, 31, 68, 0.25)",
        "glass-gold": "0 8px 32px 0 rgba(184, 134, 11, 0.20)"
      },
      backdropBlur: {
        xs: "2px"
      },
      maxWidth: {
        "8xl": "90rem"
      }
    },
    container: {
      center: true,
      padding: {
        DEFAULT: "1.25rem",
        sm: "2rem",
        md: "2.5rem",
        lg: "4rem",
        xl: "5rem",
        "2xl": "6rem"
      }
    }
  },
  plugins: []
};
