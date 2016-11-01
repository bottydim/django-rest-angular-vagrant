cd ~/wordpress
# docker run -e MYSQL_ROOT_PASSWORD=MYSQL_ROOT_PASSWORD -e MYSQL_DATABASE=wordpress --name wordpressdb -v "$PWD/database":/var/lib/mysql -d mariadb:latest
docker pull eugeneware/docker-wordpress-nginx

########## Alternatively Download separate repository
# cd ./docker-wordpress-nginx/
# docker build -t="eugeneware/docker-wordpress-nginx" .
# cd ..

docker run -p 80:80  -v /vagrant/wordpress_video:/usr/share/nginx/www  --name wordpress-nginx -d eugeneware/docker-wordpress-nginx 