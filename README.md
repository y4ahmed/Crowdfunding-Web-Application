# Team 21 Lokahi FinTech Project


### Purpose

Lokahi Fintech Crowdfunding
A System to Support Secure Crowdfunding Information Sharing between General Venture Capitalists and
Companies Seeking Investment

### Usage
This project consists of two major parts
1) The Django Web Application
2) The Local Application

### Running
To deploy the web application, follow these steps:
```python
# Clone the repo locally
git clone https://github.com/KeanF/cs3240-s17-team21.git

# Head into the 'lokahi' directory
# Go into a virtual environment. My virtual environment is called '3240'
source activate 3240

# Install all of the required modules
pip install -r requirements.txt

# Run the application through Heroku
heroku local web
