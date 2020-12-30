FROM python:3.8.7-alpine3.12
#FROM alpine:latest

#WORKDIR /

COPY .env /
COPY notesClient.py /
COPY requirements.txt /
#COPY ./file.sh /

#RUN chmod +x file.sh
RUN pip install -r requirements.txt

ENTRYPOINT python notesClient.py $1
#ENTRYPOINT ["sh", "file.sh"]