FROM nginx:alpine

RUN apk update && \
    apk add --no-cache python3 build-base python3-dev jpeg-dev zlib-dev linux-headers supervisor && \
    rm -f /tmp/* /etc/apk/cache/*

ENV VIRTUAL_HOST=blog.chengbo.net
ENV LETSENCRYPT_HOST=blog.chengbo.net
ENV LETSENCRYPT_EMAIL=chengbo1983@gmail.com

RUN mkdir -p /var/lib/nginx/cache

RUN pip3 install uwsgi
RUN pip3 install Flask==0.11.1
RUN pip3 install Markdown==2.6.7
RUN pip3 install PyYAML==3.12
RUN pip3 install beautifulsoup4==4.6.0
RUN pip3 install Pillow==4.1.1

COPY . /app
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY uwsgi.ini /etc/uwsgi/
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

WORKDIR /app

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
