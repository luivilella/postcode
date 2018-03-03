FROM python:3.6.4

EXPOSE 8080

ADD . /deploy

WORKDIR /deploy

RUN pip install -r requirements.txt

CMD python -m postcode.web_api
