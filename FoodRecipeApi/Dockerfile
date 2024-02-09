#  alpine version
FROM python:3.8-alpine  

#  Python unbuffered environment (tells python to run in unbuffered mode)
ENV PYTHONUNBUFFERED 1

#  copy the requirements from the directory adjacent to the Docker file and install all
# Install dependencies
COPY requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

#  Create a directory within our Docker image that we can use to store our application
# then switches to that as the default directory and copy app folder from the local machine to the Docker image.
RUN mkdir /app
WORKDIR /app
COPY ./app/ /app

#  Create a user which is going to be used for running application only (-D) and the switches to the user
RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN adduser -D user
RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/web
USER user
