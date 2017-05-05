FROM mxkd/uwsgi-nginx

ENV VIRTUAL_HOST=blog.chengbo.net
ENV LETSENCRYPT_HOST=blog.chengbo.net
ENV LETSENCRYPT_EMAIL=chengbo1983@gmail.com

COPY . /app

RUN pip install -r requirements.txt
