FROM python:3.11-alpine

EXPOSE 4005

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD [ "python", "src/main.py" ]