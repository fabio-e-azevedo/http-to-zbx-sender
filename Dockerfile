FROM python:3.7-alpine
COPY ./app /app
COPY ./requirements.txt /app
WORKDIR /app
RUN apk add --no-cache --virtual python3-dev g++ make
RUN pip install -U setuptools pip
RUN pip install -r requirements.txt
CMD ["python3", "main.py"]
