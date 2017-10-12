import glob
import io
import json
import os

from symplectic import posts

def _load(fname):
    with io.open(fname, "r", encoding='utf-8') as fp:
        return json.loads(fp.read())

def posts_from_json_files(fnames):
    all_posts = []
    for fname in fnames:
        all_posts.append(posts.Post(**_load(fname)))
    return all_posts
