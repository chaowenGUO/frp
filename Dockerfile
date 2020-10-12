FROM bash:latest
COPY frps /usr/local/bin/
WORKDIR /usr/local/bin/
ENTRYPOINT ./frps -p $PORT
