sudo docker pull nginx:mainline

sudo docker run -d --name jsn-dkr-run -p 8888:80 nginx:mainline

sudo docker stop jsn-dkr-run
