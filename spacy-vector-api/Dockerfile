FROM python:3
WORKDIR /usr/src/spacyapi
COPY . .
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
CMD ["python", "app.py"]