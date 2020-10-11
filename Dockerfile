FROM python:3.8

# idk
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH="/scripts:${PATH}"

# update repositories
COPY ./requirements.txt /requirements.txt
# RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN pip install -r /requirements.txt
# RUN apk del .tmp

# Config socket
COPY ./config/* /etc/systemd/system/

# Copy the app)
RUN bash -c 'mkdir -p {/etitango,/vol/web/media,/vol/web/static}'
COPY ./etitango /etitango
WORKDIR /etitango
COPY ./scripts/docker-entrypoint.sh scripts/docker-entrypoint.sh

# Add docker-compose-wait tool -------------------
# REPLACE ME after config ddbb
ENV WAIT_VERSION 2.7.2
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/$WAIT_VERSION/wait scripts/wait

RUN chmod +x scripts/*

RUN adduser --disabled-password --gecos '' etitango
RUN bash -c 'chown -R etitango:etitango {/vol,/etitango}'
RUN chmod -R 755 /vol/web
USER etitango