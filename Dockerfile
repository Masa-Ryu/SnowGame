FROM python:3.8

RUN apt-get update \
    && apt-get install -y python3-tk


WORKDIR /app

COPY ./src /app

CMD ["python", "game.py"]


