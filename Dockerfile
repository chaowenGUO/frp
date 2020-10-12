FROM bash:latest
COPY frps /usr/local/bin/
WORKDIR /usr/local/bin/
CMD ["bash", "-c", "./frps -p $PORT"]
