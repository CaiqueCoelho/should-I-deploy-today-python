# Creating requirements
pip3 freeze > requirements.txt

# Creating Virtualenv
virtualenv -p python3 venv
source venv/bin/activate
pip3 install -r requirements.txt