FROM python:3.12.3-slim

WORKDIR /app

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt


CMD ["python","test.py"]