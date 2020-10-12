FROM python:latest
COPY frps /usr/local/src/
WORKDIR /usr/local/src/
CMD ./frps -p 6000
