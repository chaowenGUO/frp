FROM python:latest
COPY frps /usr/local/src/
WORKDIR /usr/local/src/
ENTRYPOINT ./frps -p 6000
