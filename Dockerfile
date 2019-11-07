FROM centos:7

RUN yum install -y python3

COPY npc.py .
