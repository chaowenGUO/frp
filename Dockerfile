FROM bash:latest
COPY frps /usr/local/bin/
ENTRYPOINT ["bash", "-c", "frps -p $PORT"]
