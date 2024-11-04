FROM python:3.11-alpine

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /usr/src/app

COPY mongo ./mongo/
COPY discord_bot ./discord_bot/
COPY main.py .
COPY requirements.txt .

RUN apk update && apk add build-base
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Solves the problem with "No file found" error.
# Better to consider mounting
RUN mkdir logs &&\
    touch logs/discord-bot.log

CMD ["python3", "./main.py"]