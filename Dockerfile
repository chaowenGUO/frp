FROM python:latest
COPY frps /usr/local/src/
WORKDIR /usr/local/src/
ENTRYPOINT ["bash", "-c", "./frps -p $PORT"]
