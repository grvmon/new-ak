import { defineConfig } from 'astro/config';
import react from '@astrojs/react';
import keystatic from '@keystatic/astro';
import node from '@astrojs/node';
import tailwindcss from '@tailwindcss/vite';

const isGithubActions = process.env.GITHUB_ACTIONS === 'true';

export default defineConfig({
  site: isGithubActions ? 'https://grvmon.github.io' : 'http://localhost:4324',
  base: isGithubActions ? '/new-ak' : '',
  // If we are deploying to GitHub Pages, we must force static output.
  output: 'static',
  integrations: [react(), keystatic()],
  // Only use the node adapter (for Keystatic local Admin UI) if NOT building for GitHub Pages
  adapter: isGithubActions ? undefined : node({
    mode: 'standalone'
  }),
  vite: {
    plugins: [tailwindcss()]
  }
});
