FROM ubuntu:18.04
WORKDIR /app
COPY ./django-helloworld .
RUN apt update && apt install python3-dev python3-pip python3-virtualenv sqlitebrowser -y
RUN pip3 install -r requirements.txt
RUN python3 manage.py migrate
EXPOSE 8000
ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
