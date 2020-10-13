
FROM python:latest
COPY server.py /usr/local/src/
WORKDIR /usr/local/src/
RUN ["pip", "install", "aiohttp"]
ENTRYPOINT ["python", "server.py"]]
