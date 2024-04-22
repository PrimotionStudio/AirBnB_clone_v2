#!/usr/bin/env bash
# Prepare your web servers

sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir -p /var/www/html
sudo sh -c 'echo "Hello World!" > /var/www/html/index.html'
sudo sh -c 'echo "Ceci n'"i"'est pas une page" > /var/www/html/404.html';
sudo tee /etc/nginx/sites-available/default > /dev/null <<EOF
server {
    listen 80;
    listen [::]:80;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    add_header X-Served-By $HOSTNAME;
    server_name _;
    location / {
        try_files \$uri \$uri/ =404;
    }
    location /hbnb_static {
        alias /data/web_static/current/;
        autoindex off;
    }
    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4i;
    }
    error_page 404 /404.html;
    location = /404.html {
        root /var/www/html/;
        internal;
    }
}
EOF
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

if [ -L "/data/web_static/current/" ]; then
	sudo rm -f /data/web_static/current/
fi

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data

sudo service nginx start
sleep 5
sudo service nginx restart
