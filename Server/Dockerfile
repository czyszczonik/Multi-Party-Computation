FROM python:3.9-rc-buster
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
RUN pip install connexion[swagger-ui]
CMD python application.py
