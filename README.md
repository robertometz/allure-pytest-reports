# allure-pytest-reports

## Setup

$ git clone git@github.com:robertometz/allure-pytest-reports.git

$ cd allure-pytest-reports

$ python3 -m venv .venv

$ python3 -m venv .venv

$ pip install -r requirements.txt 

$ curl -o allure-2.7.0.tgz -Ls https://dl.bintray.com/qameta/generic/io/qameta/allure/allure/2.7.0/allure-2.7.0.tgz  

$ sudo tar -zxvf allure-2.7.0.tgz -C /opt/

$ sudo ln -s /opt/allure-2.7.0/bin/allure /usr/bin/allure  

$ rm allure-2.7.0.tgz

$ allure --version

$ sudo apt-get update & sudo apt-get install jq

## Run Tests

$ cp categories.json ./test_result

$ pytest --alluredir=./test_result

$ allure serve ./test_result (run locally)

## Run Docker service

$ docker-compose up -d

URL to access UI:  
http://localhost:5252/

URL to access API:  
http://localhost:5050/

## Publish test results

$ source .env

$ ./send_results.sh

## References

https://docs.qameta.io/allure/

https://github.com/fescobar/allure-docker-service

https://docs.pytest.org/en/stable/getting-started.html
