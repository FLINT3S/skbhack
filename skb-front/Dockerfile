# Build app and run unit tests
FROM cypress/base:18.12.0 AS builder

WORKDIR /app

COPY package.json yarn.lock ./

RUN yarn install

COPY . .

RUN yarn run build

# Run Cypress and unit tests
FROM builder AS test

RUN yarn run test:unit || exit 1

RUN yarn run test:e2e:nobuild || exit 1

# Serve app by Nginx
FROM nginx:1.23.2-alpine

COPY --from=builder /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
