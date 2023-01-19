FROM python:3.8.15
WORKDIR /usr/src/app


## Copy all src files
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
## Run the application on the port 8080
EXPOSE 8000

# gunicorn 배포 명령어
# CMD ["gunicorn", "--bind", "허용하는 IP:열어줄 포트", "project.wsgi:application"]
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "pragmatic.wsgi:application"]
# CMD ["python", "manage.py","runserver","0.0.0.0:8000"]
