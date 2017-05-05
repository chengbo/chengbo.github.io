FROM mxkd/uwsgi-nginx

ENV VIRTUAL_HOST=blog.chengbo.net
ENV LETSENCRYPT_HOST=blog.chengbo.net
ENV LETSENCRYPT_EMAIL=chengbo1983@gmail.com

COPY . /app
COPY nginx.conf /etc/nginx/conf.d/
COPY uwsgi.ini /etc/uwsgi/

RUN pip install -r requirements.txt
