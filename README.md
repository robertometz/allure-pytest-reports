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

## Run

$ pytest --alluredir=./test_result

$ allure serve ./test_result

## References

https://docs.qameta.io/allure/#_python

https://docs.pytest.org/en/stable/getting-started.html
