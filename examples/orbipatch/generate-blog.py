import glob

from symplectic import render, jsonformat, posts

METADATA = posts.Metadata(
    title="Local Patches of an Orbifold Life",
    description="Some small, random musing about life in an interesting "
                "place."
)

POSTS = jsonformat.posts_from_json_files(glob.glob('*.json'))
BLOG = posts.Blog(metadata=METADATA, posts=POSTS)
render.render(BLOG,
              theme='../../themes/bs4blog',
              output='../../build/blog')
