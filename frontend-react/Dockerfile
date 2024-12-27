# Use a Node.js image for React
FROM node:20-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

EXPOSE 5713

CMD ["npm", "run", "dev"]
