FROM python:3.10

RUN apt update
RUN apt install -y postgresql-client git

WORKDIR /home/root/project/

COPY ./requirements.txt ./requirements.txt

RUN pip3 install -r ./requirements.txt

EXPOSE 8003
