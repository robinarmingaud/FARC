FROM ubuntu:20.04

MAINTAINER Olivier <olivier.perraud@ingenica.fr>

ENV python=python3
ENV TZ=Europe/Paris
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
# Update the container's packages
RUN apt update; apt dist-upgrade -y

RUN apt install $python -y
RUN apt install python3-pip -y
RUN apt install python3-dev
RUN apt-get install -y python3-tk

ADD ./farc-master/farc /opt/farc/

#  RUN $python -m pip install --upgrade setuptools
# RUN $python -m pip install psutil 
RUN $python -m pip install -r /opt/farc/requirements.txt

EXPOSE 8080

WORKDIR /opt
ENTRYPOINT $python -m farc.apps.calculator





