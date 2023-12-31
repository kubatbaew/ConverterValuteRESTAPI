FROM python:3.8


ENV PYTHONUNBUFFERED 1


RUN mkdir /app
WORKDIR /app


COPY requirements.txt /app/
RUN pip install -r requirements.txt


COPY . /app/


EXPOSE 8000


CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]
