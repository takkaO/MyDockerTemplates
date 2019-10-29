# base image
FROM php:7.0-apache
# maker
MAINTAINER takkaO <hoge@hoge>
# execute command when docker build
RUN echo "** update apt source server"
RUN apt update
RUN apt upgrade -y

## is it need?
RUN echo "** install python3"
RUN apt install python3-pip -y
RUN echo "** install libs"
RUN apt install libsm6 libxext6 libxrender-dev apache2-dev -y
RUN echo "** install pip package"
RUN python3 -m pip install numpy tensorflow opencv-python chainer mod_wsgi flask pillow
RUN echo "** copy setting file"
#COPY serve-cgi-bin.conf /etc/apache2/conf-available/
COPY 000-default.conf /etc/apache2/sites-available/
COPY wsgi.load /etc/apache2/mods-available/
RUN echo "** enable wsgi"
RUN a2enmod wsgi.load