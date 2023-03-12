curl https://stepik.org/media/attachments/lesson/686238/jusan-docker-mount.conf --output jusan-docker-mount.conf

curl https://stepik.org/media/attachments/lesson/686238/jusan-docker-mount.zip --output jusan-docker-mount.zip


sudo sudo docker run -d \
  -p 9999:80 \
 -it \
  --name jusan-docker-mount \
--mount type=bind,source="$(pwd)"/jusan-docker-mount.conf,target=/etc/nginx/conf.d/default.conf \
--mount type=bind,source="$(pwd)"/jusan-docker-mount,target=/var/www/example \
nginx:mainline
