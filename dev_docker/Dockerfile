FROM python:3.9-slim-buster

WORKDIR /app

RUN pip install opencv-python

COPY script.py .

EXPOSE 80

CMD ["python". "script.py"]

