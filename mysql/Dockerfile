FROM mysql:latest
VOLUME ["/docker-entrypoint-initdb.d"]
CMD ["CHARACTER SET utf8"]
COPY ./mysql/1_db_countries_countries.sql /docker-entrypoint-initdb.d/
COPY ./mysql/2_db_countries_provinces.sql /docker-entrypoint-initdb.d/
COPY ./mysql/3_db_countries_cities.sql /docker-entrypoint-initdb.d/