FROM centos:latest
MAINTAINER Wesley Dugan
WORKDIR /tmp
ADD ./bin /tmp/

RUN yum update -y \
    && yum upgrade -y \
    && yum install python3 -y \
    && pip3 install requests

ENTRYPOINT ./discordposter.py  
