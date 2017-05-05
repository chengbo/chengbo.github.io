import os
import re
import yaml
import glob
from flask import Flask, render_template, url_for, send_from_directory
from post import Post
from pagination import Pagination


app = Flask(__name__)
app.config['SITE_TITLE'] = 'Inspiration from life'


def _parse_meta(meta):
    return yaml.load(meta)


def _read_post(file):
    with open(file, "r") as f:
        file_content = f.read()
    m = re.match(r'---(.*)\n---\n(.*)', file_content, re.DOTALL)
    meta = _parse_meta(m.group(1))
    meta['file_name'] = os.path.splitext(os.path.basename(file))[0]
    content = m.group(2)
    return Post(meta, content)


def url_for_other_page(page):
    if page == 1:
        return url_for('home')
    return url_for('page', page_number=page)


app.jinja_env.globals['url_for_other_page'] = url_for_other_page

all_posts = []
all_tags = {}
for path in glob.iglob(app.root_path + '/content/**/*.md', recursive=True):
    post = _read_post(path)
    all_posts.append(post)
    if 'tags' not in post.meta:
        continue
    for tag in post.meta['tags']:
        if tag in all_tags:
            all_tags[tag].append(post)
        else:
            all_tags[tag] = [post]

all_posts.sort(key=lambda post: post.meta['date'], reverse=True)


@app.route('/', endpoint='home')
@app.route('/page/', defaults={'page_number': 1})
@app.route('/page/<int:page_number>')
def page(page_number=1):
    total_count = len(all_posts)
    page_size = 10
    posts = all_posts[(page_number - 1) * page_size:page_number * page_size]
    if not posts:
        return render_template('404.html'), 404
    pagination = Pagination(page_number, page_size, total_count)
    return render_template('index.html',
                           posts=posts,
                           pagination=pagination)


@app.route('/about')
def about():
    path = '{}/content/about/index.md'.format(app.root_path)
    post = _read_post(path)
    return render_template('post.html', post=post)


@app.route('/<year>/<month>/<day>/<title>.html')
def post(year, month, day, title):
    path = '{}/content/{}/{}/{}/{}.md'.format(app.root_path, year, month, day, title)
    post = _read_post(path)
    return render_template('post.html', post=post)


@app.route('/tag/<tag>')
def tag(tag):
    posts = all_tags[tag]
    return render_template('index.html', posts=posts)


@app.route('/images/<path:path>')
def send_js(path):
    return send_from_directory('static/images', path)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
