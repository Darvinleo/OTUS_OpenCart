### This is my education repo with some automation tests for the "OpenCart" ###
I used the OpenCart version [packaged by Bitnami](https://hub.docker.com/r/bitnami/opencart/) just for my educational purposes.
If you for some reason want to download and run my tests, below are steps that you need to do:
1. Ensure that you have installed on your host python3, docker and docker-compose 
2. Than clone this repo:<br/>
` git clone https://github.com/Darvinleo/OTUS_OpenCart `<br/>
3. After that from dir with repo execute:<br/>
 `docker-compose up -d`<br/>
`pip install -r requiremenets.txt`<br/>
`pytest`<br/>

You must have internet access and no local proxy