# Team 21 Lokahi FinTech Project


### Purpose

Lokahi Fintech Crowdfunding
A System to Support Secure Crowdfunding Information Sharing between General Venture Capitalists and
Companies Seeking Investment

### Usage
This project consists of two major parts
1) The Django Web Application
2) The Local Application

### Requirement(s)
Anaconda (for Python 3.5)

### Running
To deploy the web application, follow these steps:
```python
# Clone the repo locally
git clone https://github.com/KeanF/cs3240-s17-team21.git

# Head into the 'lokahi_dropbox' directory
# Create a virtual environment. My virtual environment is called '3240'
conda create --name cs3240 python=3.5 --file conda-requirements.txt

# Activate virutal environment
source activate 3240

# Install remaining required modules
pip install -r requirements.txt

# Create default SiteManager role
python manage.py loaddata fixtures/users.json
python manage.py loaddata fixtures/base_users.json

# Run the application through Heroku
heroku local web 
