import glob

import symplectic
from symplectic import jsonformat

METADATA = symplectic.Metadata(
    title="Local Patches of an Orbifold Life",
    description="Some small, random musing about life in an interesting "
                "place."
)

POSTS = jsonformat.posts_from_json_files(glob.glob('*.json'))
BLOG = symplectic.Blog(metadata=METADATA, posts=POSTS)
symplectic.render(BLOG,
                  theme='../../themes/bs4blog',
                  output='../../build/blog')
