FROM python:3.10
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY sh/requirements.txt /code/
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
COPY sh /code/sh
RUN pip install --upgrade pip && cd /code/sh && sh ./install_prerequirements.sh
RUN jupyter nbextension enable --py widgetsnbextension
