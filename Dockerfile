FROM python:latest
COPY frps frps.ini /usr/local/src/
WORKDIR /usr/local/src/
ENTRYPOINT ["./frps", "-p", "$PORT"]
