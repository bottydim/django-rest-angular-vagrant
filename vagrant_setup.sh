###############################################
# Install Pip3
###############################################
echo "install pip3"

sudo apt-get -y install python3-pip


###############################################
# Install NodeJS
###############################################
echo "install NODEJS"
curl --silent --location https://deb.nodesource.com/setup_7.x | sudo bash -
sudo apt-get -y install nodejs
# ln -s /usr/bin/nodejs /usr/bin/node
# Add node_modules to environment variables
echo "export NODE_PATH=/usr/local/lib/node_modules" >> ~/.bashrc

echo "install build-essential"
sudo apt-get install -y build-essential

###############################################
# Install NPM
###############################################
echo "install NPM"
# sudo apt-get -y install npm

###############################################
# Setup PostgreSQL
###############################################
sudo apt-get update
sudo apt-get -y install python-pip python-dev libpq-dev postgresql postgresql-contrib python-psycopg2 python3-psycopg2
sudo apt-get update
sudo apt-get -y upgrade

### Upgrade PIP
sudo pip install --upgrade pip

## Install Django PIP
sudo pip install django psycopg2

## Upgrade Django
sudo pip install --upgrade django

## Upgrade Psycopg2
sudo pip install --upgrade psycopg2

## Install Rest_framework PIP
sudo pip install djangorestframework

## Upgrade Rest_framework
sudo pip3 install --upgrade djangorestframework

## Installing dependencies for PostgreSQL
sudo apt-get -y install libpq-dev python3-dev
sudo apt-get -y install postgresql-server-dev-all

## Install Graphical Interface for PostgreSQL
sudo apt-get -y install pgadmin3


# # download and install docker 
# sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
# echo "deb https://apt.dockerproject.org/repo ubuntu-trusty main" | sudo tee /etc/apt/sources.list.d/docker.list
# sudo apt-get update
# sudo apt-get install docker-engine -y


# # Add vagrant user to the docker group
# sudo groupadd docker
# sudo usermod -aG docker $USER

# # install docker-compose
# # https://docs.docker.com/engine/installation/linux/ubuntulinux/
# curl -L "https://github.com/docker/compose/releases/download/1.8.1/docker-compose-$(uname -s)-$(uname -m)" > /usr/local/bin/docker-compose
# chmod +x /usr/local/bin/docker-compose

# # make it possible to connect from PyCharm to docker
# config_line='DOCKER_OPTS="-H tcp://0.0.0.0:2375 -H unix:///var/run/docker.sock"'
# already_added=$(cat /etc/default/docker | grep $config_line)

# if [[ $already_added ]] ; then
# 	echo ""
# else
# 	 echo $config_line > /etc/default/docker
# fi


# # install heroku toolbelt
# #wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh

# folder_to_use=$1
# if [[ $folder_to_use ]] ; then
# 	# $1 is the first argument passed to the script 
# 	cmd="cd $folder_to_use"
# 	# open the specified folder on ssh-ing into the virtual machine
# 	echo $cmd >> '/home/vagrant/.bashrc'
# fi
# # add useful aliases to the bashrc. they are for one-off commands against docker containers.
# echo "alias shell='docker-compose run --no-deps --rm web python manage.py shell'" >> '/home/vagrant/.bashrc'
# echo "alias init_db='docker-compose run --no-deps --rm web python manage.py init_db'" >> '/home/vagrant/.bashrc'
# echo "alias drop_db='docker-compose run --no-deps --rm web python manage.py drop_db'" >> '/home/vagrant/.bashrc'
# echo "alias drop_and_init_db='docker-compose run --no-deps --rm web python manage.py drop_and_init_db'" >> '/home/vagrant/.bashrc'
# echo "$1 added as default ssh init folder AND drop_and_init_db, init_db, drop_db and shell aliases added."


# echo "Do vagrant reload now"
