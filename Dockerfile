FROM python:3.10-slim

RUN apt-get update && apt-get install -y git && apt-get clean

WORKDIR /

RUN git clone https://github.com/Abysmalll/sqli.git /app

WORKDIR /app

RUN pip install --no-cache-dir flask

EXPOSE 80

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "80"]