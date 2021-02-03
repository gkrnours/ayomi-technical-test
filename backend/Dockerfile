FROM python:3.9
RUN groupadd -r alice && useradd --no-log-init -r -g alice -u 1000 alice
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/