FROM node:16-alpine as build-step
WORKDIR ./frontend
COPY ./frontend ./
RUN yarn install
RUN yarn build

FROM python:3.10.4
WORKDIR ./app
COPY --from=build-step ./frontend/build ./frontend/build
COPY ./backend ./backend
RUN pip install -r ./backend/requirements.txt

WORKDIR ./backend
EXPOSE 5000