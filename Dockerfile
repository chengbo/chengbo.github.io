FROM nginx:alpine

RUN apk update && \
    apk add --no-cache python3 py3-pip build-base python3-dev jpeg-dev zlib-dev linux-headers supervisor && \
    rm -f /tmp/* /etc/apk/cache/*

ENV VIRTUAL_HOST=blog.chengbo.net
ENV LETSENCRYPT_HOST=blog.chengbo.net
ENV LETSENCRYPT_EMAIL=chengbo1983@gmail.com

RUN mkdir -p /var/lib/nginx/cache

RUN pip3 install uwsgi
RUN pip3 install Flask==2.3.3
RUN pip3 install Markdown==3.4.4
RUN pip3 install PyYAML==6.0.1
RUN pip3 install beautifulsoup4==4.12.2
RUN pip3 install Pillow==10.0.0

COPY . /app
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY uwsgi.ini /etc/uwsgi/
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

WORKDIR /app

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
