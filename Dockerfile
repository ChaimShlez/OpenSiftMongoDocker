FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt --no-cache-dir --upgrade mysql-connector-python

COPY . .



EXPOSE 8000

CMD ["uvicorn", "services.data_loader.app:app", "--host", "0.0.0.0", "--port", "8000"]

