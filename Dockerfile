FROM python:3

# idk
ENV PYTHONUNBUFFERED 1

# update repositories
RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev mysql-common -y
RUN pip install pip -U

# Copy the app, connect to the data base (only for dev)
COPY etitango /var/www/html/etitango
COPY requirements.txt /var/www/html/etitango/
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN ln -s /usr/local/bin/docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh

# Add docker-compose-wait tool -------------------
ENV WAIT_VERSION 2.7.2
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/$WAIT_VERSION/wait /wait
RUN chmod +x /wait

# ENTRYPOINT ["docker-entrypoint.sh"]
