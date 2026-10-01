import { defineConfig } from 'astro/config';
import react from '@astrojs/react';
import keystatic from '@keystatic/astro';
import node from '@astrojs/node';
import tailwindcss from '@tailwindcss/vite';

const isGithubActions = process.env.GITHUB_ACTIONS === 'true';

export default defineConfig({
  site: isGithubActions ? 'https://grvmon.github.io' : 'http://localhost:4324',
  base: isGithubActions ? '/new-ak' : '',
  integrations: [react(), keystatic()],
  adapter: node({
    mode: 'standalone'
  }),
  vite: {
    plugins: [tailwindcss()]
  }
});
