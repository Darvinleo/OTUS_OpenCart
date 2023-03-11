### This is my education repository containing several automation scripts for UI and backend tests of "OpenCart"

I used the OpenCart version [packaged by Bitnami](https://hub.docker.com/r/bitnami/opencart/) just for my educational
purposes.
The tests are written using the pytest framework for test automation, Selenium for UI testing, PyMySQL for database
validation and Allure for generating test-reports<br/>
If you for some reason want to download and run my tests, below are steps that you need to do:/

#### Ensure that you have installed on your host python >=3.10, docker and docker-compose </br> You must have internet access and no local proxy <br/>

1. Clone this repo:<br/>
   ` git clone https://github.com/Darvinleo/OTUS_OpenCart `<br/>
2. After that go to the cloned dir and run:<br/>
   `docker-compose up -d`<br/>
3. Create virtualenv for this project and install requirements: <br/>
   `python3 -m venv .venv` <br/>
   `source .venv/bin/activate` <br/>
   `pip install -r requiremenets.txt`<br/>
4. Finally, you can run tests: <br/>
   `pytest`<br/>