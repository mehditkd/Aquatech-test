FROM python:latest

COPY src /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT flask run --host 0.0.0.0
