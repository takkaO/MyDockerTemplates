# base image
FROM php:7.0-apache
# maker
MAINTAINER okuyama <hoge@hoge>
# execute command when docker build
RUN echo "change apt source server"
RUN apt update
RUN apt upgrade -y

## is it need?
RUN echo "install python3"
RUN apt install python3-pip -y
RUN echo "install libs"
RUN apt install libsm6 libxext6 libxrender-dev -y
RUN echo "install pip package"
RUN python3 -m pip install numpy tensorflow opencv-python