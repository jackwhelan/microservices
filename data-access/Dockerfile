FROM python:3.10.0-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src/* .
ENTRYPOINT [ "python" ]
CMD [ "server.py" ]