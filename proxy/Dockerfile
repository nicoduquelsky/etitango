FROM nginx:1.19.0-alpine

RUN rm /etc/nginx/conf.d/default.conf

USER root

RUN mkdir -p /vol/web/static
RUN chmod 755 /vol/web/static

# USER nginx