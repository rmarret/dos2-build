from flask import Flask, render_template, request, send_from_directory, send_file, url_for
from flask_weasyprint import HTML, render_pdf
import yaml
from os import path
from io import BytesIO
import imgkit
import json


app = Flask(__name__)

with open('database/database.json') as f:
    db = json.loads(f.read())


def get_image(name):
    key = '_'.join(name.split(' ')).lower()
    for k in db.keys():
        for entry in db[k]:
            if entry['key'] == key:
                return entry['image']
    return ""


def get_images_and_texts(list):
    images = []
    texts = []
    for k in list:
        img = get_image(k)
        if img:
            images.append(img)
        else:
            texts.append(k)
    return images, texts


def get_build(name):
    name = 'database/' + name + ('.yaml' if not name.endswith('.yaml') else '')
    if not path.exists(name):
        return None
    with open(name, 'r', encoding = 'utf-8') as f:
        document = yaml.safe_load(f)
    return document


@app.route('/build/', defaults={'name': 'juggernaut'})
@app.route('/build/<name>')
def index(name):
    build = get_build(name)
    if build is None:
        return 'Unknown build'
    return render_template('build.html', build=list(build.values())[0], get_image=get_image, get_images_and_texts=get_images_and_texts)

@app.route('/dl/', defaults={'name': ''})
@app.route('/dl/<name>')
def image(name):
    options = {
        'format': 'png',
    }
    img = imgkit.from_url(request.url_root + '/build/' + name, False, options=options)
    #img = imgkit.from_string(index(), False, options=options)
    #return send_file(img, attachment_filename='build.png')
    return send_file(
        BytesIO(img),
        mimetype='image/png',
        as_attachment=False,
        attachment_filename='%s.png' % 'build')


@app.route('/pdf/<name>')
def pdf(name):
    html = index(name)
    return render_pdf(HTML(string=html))
