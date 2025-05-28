FROM node:18-alpine
WORKDIR /app
COPY package.json .
RUN npm install
COPY public ./public
COPY src/main.js ./public/main.js
EXPOSE 8000
CMD ["npx", "serve", "public", "-l", "8000"] 