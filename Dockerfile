FROM ubuntu:latest

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 627220E7
RUN apt-get update 
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y apt-transport-https ca-certificates procps python-pip
RUN echo 'deb http://archive.scrapy.org/ubuntu scrapy main' | tee /etc/apt/sources.list.d/scrapy.list
RUN apt-get update 
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y scrapy-0.24

