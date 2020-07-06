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

# Add docker-compose-wait tool -------------------
ENV WAIT_VERSION 2.7.2
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/$WAIT_VERSION/wait /wait
RUN chmod +x /wait

RUN pip install -r /var/www/html/etitango/requirements.txt
CMD ["python3", "/var/www/html/etitango/manage.py", "makemigrations"]
CMD ["python3", "/var/www/html/etitango/manage.py", "migrate"]
