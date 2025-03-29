FROM node:18

WORKDIR /app

COPY api/frontend/intuitive_care/package*.json ./

RUN npm install

COPY api/frontend/intuitive_care/ ./

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
