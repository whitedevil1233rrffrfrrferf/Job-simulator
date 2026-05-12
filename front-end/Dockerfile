FROM node:20

WORKDIR /app

COPY package*.json .

RUN npm install

COPY . .

ENV WATCHPACK_POLLING=true
ENV CHOKIDAR_USEPOLLING=true
ENV NEXT_DISABLE_TURBOPACK=1

EXPOSE 3000

CMD ["npm", "run", "dev"]
