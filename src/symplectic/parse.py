import glob
import io
import json
import os

from symplectic import render

def load(fname):
    with io.open(fname, "r", encoding='utf-8') as fp:
        return json.loads(fp.read())

def parse(place):
    metadata = load(os.path.join(place, 'metadata.json'))
    posts = []
    for fname in glob.glob(os.path.join(place, '*.json')):
        if fname.endswith('metadata.json'):
            continue
        posts.append(load(fname))
    return render.Blog(metadata=render.Metadata(**metadata),
                       posts=[render.Post(**post) for post in posts])
