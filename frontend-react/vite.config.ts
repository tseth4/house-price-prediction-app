import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import * as path from 'path'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    host: '0.0.0.0', // Expose to all network interfaces
    port: 5173,      // Optional: Specify the port
  },
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src/')
    },
  },

})
