import functools
import glob
import io
import json
import os

from symplectic import posts

def _load(fname):
    with io.open(fname, "r", encoding='utf-8') as fp:
        return json.loads(fp.read())

def _load_with_klass(klass, names):
    return [klass(**_load(name)) for name in names]

posts_from_json_files = functools.partial(_load_with_klass, posts.Post)
pages_from_json_files = functools.partial(_load_with_klass, posts.Page)
