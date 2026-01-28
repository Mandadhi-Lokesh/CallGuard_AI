/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        brand: {
          background: '#0a0f1c', // Very dark blue/black
          card: '#111827', // Dark blue/grey for cards
          text: '#f8fafc', // White/slate-50
          muted: '#94a3b8', // Slate-400
          accent: '#3b82f6', // Blue-500
          success: '#10b981',
          warning: '#f59e0b',
          danger: '#ef4444',
        }
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
      }
    },
  },
  plugins: [],
}
