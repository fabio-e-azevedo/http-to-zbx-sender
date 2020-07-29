FROM python:3.8-alpine

COPY ./src /app
COPY ./requirements.txt /app

WORKDIR /app

RUN apk add --no-cache --virtual build-deps python3-dev g++ make && \
    pip install --no-cache-dir -U setuptools pip && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del build-deps

CMD ["python3", "main.py"]
