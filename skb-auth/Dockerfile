FROM python:3.10.8-alpine3.16

WORKDIR /app

RUN apk update && \
    apk add --virtual build-deps gcc musl-dev && \
    apk add postgresql-dev

COPY requierements.txt requierements.txt

RUN pip install -r requierements.txt

COPY . .

EXPOSE 5000

CMD ["uvicorn", "main:api.app", "--host", "0.0.0.0", "--port", "5000", "--reload"]
