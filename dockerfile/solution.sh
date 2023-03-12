<h1> Dockerfile <h1>

FROM nginx:mainline

WORKDIR /usr/src/app

COPY ./dockerfile.conf  /etc/nginx/conf.d/default.conf

COPY ./jusan-dockerfile/ /var/www/jusan-dockerfile

EXPOSE 6060



<h1>CLI<h1>

sudo docker build . -t nginx:jusan-dockerfile`

sudo docker run -d -p 6060:80 --name jusan-dockerfile nginx:jusan-dockerfile
