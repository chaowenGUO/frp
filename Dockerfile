FROM python:latest
COPY frps frps.ini /usr/local/src/
WORKDIR /usr/local/src/
ENTRYPOINT ["bash", "-c", "./frps -p $PORT"]
