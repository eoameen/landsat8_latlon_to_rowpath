FROM ubuntu:18.04

# Install GDAL 2.1 for python 2 & 3
RUN \
  apt -y update --fix-missing && \
  apt -y install software-properties-common && \
  apt -y update && \
  apt -y upgrade && \
  apt -y install gdal-bin libgdal-dev python-gdal python3-gdal python3-pip libsm6 libxext6 libxrender-dev && \
  rm -rf /var/lib/apt/lists/*

WORKDIR /workspace
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# Copy files
COPY . /workspace
