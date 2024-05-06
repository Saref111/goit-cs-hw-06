FROM python:3.9-slim

COPY server.py /app/
COPY index.html /app/
COPY message.html /app/
COPY style.css /app/
COPY logo.png /app/
COPY error.html /app/

WORKDIR /app

RUN pip install pymongo

CMD ["python", "server.py"]
