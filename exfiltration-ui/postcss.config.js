import tailwindcss from '@tailwindcss/postcss';
import autoprefixer from 'autoprefixer';

/** @type {import('postcss').Processor} */
export default {
  plugins: [
    tailwindcss(),
    autoprefixer(),
  ],
};

