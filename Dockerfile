FROM python:latest
COPY frps /usr/local/src/
WORKDIR /usr/local/src/
ENV port $PORT
ENTRYPOINT ./frps -p port
