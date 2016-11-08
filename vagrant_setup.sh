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
sudo apt-get -y install postgresql postgresql-contrib python3-psycopg2
sudo apt-get update
sudo apt-get -y upgrade

## Installing dependencies for PostgreSQL
sudo apt-get -y install libpq-dev python3-dev
sudo apt-get -y install postgresql-server-dev-all

## Install Graphical Interface for PostgreSQL
sudo apt-get -y install pgadmin3

###############################################
# PostgreSQL Creating a DB
###############################################
# Edit the following to change the name of the database user that will be created:
APP_DB_USER=myapp
APP_DB_PASS=dbpass

# Edit the following to change the name of the database that is created (defaults to the user name)
APP_DB_NAME=$APP_DB_USER

# Edit the following to change the version of PostgreSQL that is installed
PG_VERSION=9.5

###########################################################
# Changes below this line are probably not necessary
###########################################################
print_db_usage () {
  echo "Your PostgreSQL database has been setup and can be accessed on your local machine on the forwarded port (default: 15432)"
  echo "  Host: localhost"
  echo "  Port: 5432"
  echo "  Database: $APP_DB_NAME"
  echo "  Username: $APP_DB_USER"
  echo "  Password: $APP_DB_PASS"
  echo ""
  echo "Admin access to postgres user via VM:"
  echo "  vagrant ssh"
  echo "  sudo su - postgres"
  echo ""
  echo "psql access to app database user via VM:"
  echo "  vagrant ssh"
  echo "  sudo su - postgres"
  echo "  PGUSER=$APP_DB_USER PGPASSWORD=$APP_DB_PASS psql -h localhost $APP_DB_NAME"
  echo ""
  echo "Env variable for application development:"
  echo "  DATABASE_URL=postgresql://$APP_DB_USER:$APP_DB_PASS@localhost:5432/$APP_DB_NAME"
  echo ""
  echo "Local command to access the database via psql:"
  echo "  PGUSER=$APP_DB_USER PGPASSWORD=$APP_DB_PASS psql -h localhost -p 5432 $APP_DB_NAME"
}

export DEBIAN_FRONTEND=noninteractive

PROVISIONED_ON=/etc/vm_provision_on_timestamp
if [ -f "$PROVISIONED_ON" ]
then
  echo "VM was already provisioned at: $(cat $PROVISIONED_ON)"
  echo "To run system updates manually login via 'vagrant ssh' and run 'apt-get update && apt-get upgrade'"
  echo ""
  print_db_usage
  exit
fi

PG_REPO_APT_SOURCE=/etc/apt/sources.list.d/pgdg.list
if [ ! -f "$PG_REPO_APT_SOURCE" ]
then
  # Add PG apt repo:
  echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" > "$PG_REPO_APT_SOURCE"

  # Add PGDG repo key:
  wget --quiet -O - https://apt.postgresql.org/pub/repos/apt/ACCC4CF8.asc | apt-key add -
fi

# Update package list and upgrade all packages
apt-get update
apt-get -y upgrade

apt-get -y install "postgresql-$PG_VERSION" "postgresql-contrib-$PG_VERSION"

PG_CONF="/etc/postgresql/$PG_VERSION/main/postgresql.conf"
PG_HBA="/etc/postgresql/$PG_VERSION/main/pg_hba.conf"
PG_DIR="/var/lib/postgresql/$PG_VERSION/main"

# Edit postgresql.conf to change listen address to '*':
sed -i "s/#listen_addresses = 'localhost'/listen_addresses = '*'/" "$PG_CONF"

# Append to pg_hba.conf to add password auth:
echo "host    all             all             all                     md5" >> "$PG_HBA"

# Explicitly set default client_encoding
echo "client_encoding = utf8" >> "$PG_CONF"

# Restart so that all new config is loaded:
service postgresql restart

cat << EOF | su - postgres -c psql
-- Create the database user:
CREATE USER $APP_DB_USER WITH PASSWORD '$APP_DB_PASS';

-- Create the database:
CREATE DATABASE $APP_DB_NAME WITH OWNER=$APP_DB_USER
                                  LC_COLLATE='en_US.utf8'
                                  LC_CTYPE='en_US.utf8'
                                  ENCODING='UTF8'
                                  TEMPLATE=template0;
EOF

# Tag the provision time:
date > "$PROVISIONED_ON"

echo "Successfully created PostgreSQL dev virtual machine."
echo ""
print_db_usage


###############################################
# Setup Python
###############################################
sudo pip3 install -r /vagrant/requirements.txt


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
