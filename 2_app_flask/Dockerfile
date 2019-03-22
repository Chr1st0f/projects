FROM python:3
MAINTAINER totof <christophe.cazin@cyber-secu.com>

WORKDIR /app
# Copy the content of current directory on /app into the container 
ADD . /app


RUN pip install --no-cache-dir -r /app/requirements.txt
