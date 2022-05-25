FROM node:16-alpine as build-step
WORKDIR /frontend
COPY ./ ./
RUN yarn install
RUN yarn build

FROM nginx:stable-alpine
COPY --from=build-step /frontend/build /usr/share/nginx/html
COPY deployment/nginx.default.conf /etc/nginx/conf.d/default.conf