import glob
import io
import json
import os

from symplectic import posts

def load(fname):
    with io.open(fname, "r", encoding='utf-8') as fp:
        return json.loads(fp.read())

def parse(place):
    metadata = load(os.path.join(place, 'metadata.json'))
    all_posts = []
    for fname in glob.glob(os.path.join(place, '*.json')):
        if fname.endswith('metadata.json'):
            continue
        all_posts.append(load(fname))
    return posts.Blog(metadata=posts.Metadata(**metadata),
                      posts=[posts.Post(**post) for post in all_posts])
