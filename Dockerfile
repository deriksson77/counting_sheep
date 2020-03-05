FROM centos/python-35-centos7:latest

COPY . /tmp/

RUN /tmp/counting_sheep.py
