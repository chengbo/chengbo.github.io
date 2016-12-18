import os
import re
import yaml
import glob
from flask import Flask, render_template
from post import Post

app = Flask(__name__)


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

all_posts = []
for path in glob.iglob(app.root_path + '/content/**/*.md', recursive=True):
    post = _read_post(path)
    all_posts.append(post)

all_posts.sort(key=lambda post: post.meta['date'], reverse=True)


@app.route("/")
def posts():
    return render_template('index.html', posts=all_posts[:10])


@app.route('/<year>/<month>/<day>/<title>.html')
def post(year, month, day, title):
    path = '{}/content/{}/{}/{}/{}.md'.format(app.root_path, year, month, day, title)
    post = _read_post(path)
    return render_template('post.html', post=post)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
