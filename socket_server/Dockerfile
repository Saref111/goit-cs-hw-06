FROM python:3.9-slim

COPY socket_server.py /app/

RUN pip install pymongo

WORKDIR /app

CMD ["python", "app/socket_server.py"]
