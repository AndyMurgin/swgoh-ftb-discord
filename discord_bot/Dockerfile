FROM python:3-alpine

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /usr/src/app

COPY . .

RUN apk update && apk add build-base

RUN pip install -r requirements.txt

#CMD ["ls", "-la", "."]
CMD ["python3", "./main.py"]