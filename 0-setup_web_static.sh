#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

# Installing nginx
apt-get update
apt-get install -y nginx

# Creating folders
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# testing our nginx congiguration with a simple content
echo "Setting up our web servers" > /data/web_static/releases/test/index.html

# creating a symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Ownerships and groups
chown -R ubuntu /data/
chgrp -R ubuntu /data/

# updating nginx
printf %s "server {
     listen 80 default_server;
     listen [::]:80 default_server;
     add_header X-Served-By $HOSTNAME;
     root /var/www/html;
     index index.html index.htm;
     location /hbnb_static {
     	alias /data/web_static/current;
	index index.html index.htm
     }
     location /redirect_me {
     	return 301 https://github.com/Mosesomo;
     }
     error_page 404 /404.html
     location /404 {
     	root /var/www/html;
	internal;
     }
}" > /etc/nginx/sites-available/default

# restarting our server
service nginx restart
