import glob
import shutil

import symplectic
from symplectic import jsonformat, rest

METADATA = symplectic.Metadata(
    title="Local Patches of an Orbifold Life",
    description="Some small, random musing about life in an interesting "
                "place.",
    links=[("GitHub", "https://github.com/moshez")],
)

POSTS = jsonformat.posts_from_json_files(glob.glob('*.json'))
POSTS += rest.posts_from_rest_files(glob.glob('*.rst'))
POSTS.sort(key=lambda post: post.date, reverse=True)
PAGES = jsonformat.pages_from_json_files(glob.glob('pages/*.json'))
PAGES += rest.pages_from_rest_files(glob.glob('pages/*.rst'))
BLOG = symplectic.Blog(metadata=METADATA, posts=POSTS, pages=PAGES)
symplectic.render(BLOG,
#                  theme='../../themes/bs4blog',
                  theme=['../../themes/basic', '../../themes/bs4blog'],
                  output='../../build/blog')
shutil.copy('../../build/blog/river.html', '../../build/blog/index.html')
