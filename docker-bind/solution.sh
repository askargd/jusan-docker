sudo docker run -d \
  -p 7777:80 \
  -it \
  --name jusan-docker-bind \
  --mount type=bind,source="$(pwd)"/nginx.conf,target=/etc/nginx/nginx.conf \
  nginx:latest
