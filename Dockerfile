FROM python:3.12-alpine3.20

RUN apk add postgresql-dev gcc python3-dev musl-dev

RUN addgroup -S app && adduser -S app -u 1000 -h /home/app -G app && \
    chown -R app: /home/app && \
    mkdir -p /usr/src/app && \
    chown -R app: /usr/src/app

WORKDIR /usr/src/app

USER app

COPY requirements.txt ./

RUN python3 -m pip install -r requirements.txt --no-cache-dir

COPY . .

CMD ["sh", "./docker-entrypoint.sh"]
