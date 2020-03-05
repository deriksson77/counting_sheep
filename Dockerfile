FROM centos/python-35-centos7:latest

COPY . /tmp/

CMD [ "python" "/tmp/counting_sheep.py" ]
