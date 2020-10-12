FROM nginx:1.19.0-alpine

RUN rm /etc/nginx/conf.d/default.conf

USER root

RUN mkdir -p /var/www/html/{static,media}
RUN chmod -R 755 /var/www/html

# USER nginx