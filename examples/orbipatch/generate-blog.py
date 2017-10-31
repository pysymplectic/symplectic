import glob

import symplectic
from symplectic import jsonformat

METADATA = symplectic.Metadata(
    title="Local Patches of an Orbifold Life",
    description="Some small, random musing about life in an interesting "
                "place.",
    links=[("GitHub", "https://github.com/moshez")],
)

POSTS = jsonformat.posts_from_json_files(glob.glob('*.json'))
POSTS.sort(key=lambda post: post.date, reverse=True)
PAGES = jsonformat.pages_from_json_files(glob.glob('pages/*.json'))
BLOG = symplectic.Blog(metadata=METADATA, posts=POSTS, pages=PAGES)
symplectic.render(BLOG,
                  theme='../../themes/bs4blog',
                  output='../../build/blog')
