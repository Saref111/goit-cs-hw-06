FROM python:3.9-slim

COPY socket_server.py /app/

WORKDIR /app

RUN pip install pymongo

CMD ["python", "socket_server.py"]