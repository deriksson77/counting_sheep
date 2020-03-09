FROM python:3

ADD counting_sheep.py /

CMD [ "python", "./counting_sheep.py" ]
