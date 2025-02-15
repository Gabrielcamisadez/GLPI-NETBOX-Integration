FROM php:7.4-apache

RUN apt-get update && apt-get install -y \
    libldap2-dev \
    libbz2-dev \
    libpng-dev \
    libjpeg-dev \
    libfreetype6-dev \
    libicu-dev \
    libxml2-dev \
    zlib1g-dev \
    libssl-dev \
    && docker-php-ext-install ldap bz2 gd intl xml opcache mysqli pdo pdo_mysql \
    && docker-php-ext-enable opcache mysqli pdo pdo_mysql

RUN a2enmod rewrite

COPY . /var/www/html/

RUN mkdir -p /var/www/html/files /var/www/html/config \
    && chown -R www-data:www-data /var/www/html/files /var/www/html/config \
    && chmod -R 755 /var/www/html/files /var/www/html/config \
    && chmod -R 777 /var/www/html/files \
    && chmod -R 777 /var/www/html/config

EXPOSE 80

ENV GLPI_DB_HOST=db
ENV GLPI_DB_NAME=glpi
ENV GLPI_DB_USER=glpi
ENV GLPI_DB_PASSWORD=glpi

CMD ["apache2-foreground"]
