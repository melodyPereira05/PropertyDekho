sudo apt-get update
sudo apt install python3-pip -y
sudo pip3 install virtualenv 

alias python="python3"
#Create environment
python -m venv env
source env/bin/activate
# Install requirements
pip install -r requirements.txt
# start server
python manage.py runserver 8080