cd /vagrant

sudo pip3 install -r requirements.txt
cd exampleapp
python3 manage.py migrate
python3 manage.py runserver &

#set up Angular

cd ../angular2
npm install
npm start &