import os
import shutil

import attr

import chameleon

def process(template_file, inputs, output_file):
    with open(template_file) as fp:
        template_str = fp.read()
    template = chameleon.PageTemplate(template_str)
    rendered = template(**inputs)
    with open(output_file, 'w') as fp:
        fp.write(rendered)

@attr.s(frozen=True)
class Post(object):
    title = attr.ib()
    slug = attr.ib()
    date = attr.ib()
    author = attr.ib()
    contents = attr.ib()

    @property
    def rel_link(self):
        return self.slug + '.html'

@attr.s(frozen=True)
class Metadata(object):
    title = attr.ib()
    description = attr.ib()

@attr.s(frozen=True)
class Blog(object):
    metadata = attr.ib()
    posts = attr.ib()

def render(blog, theme, output):
    if not os.path.exists(output):
        os.makedirs(output)
    process(os.path.join(theme, 'river.html'),
            dict(metadata=blog.metadata, posts=blog.posts),
            os.path.join(output, 'river.html'))
    process(os.path.join(theme, 'list.html'),
            dict(metadata=blog.metadata, posts=blog.posts),
            os.path.join(output, 'list.html'))
    for i, post in enumerate(blog.posts):
        process(os.path.join(theme, 'post.html'),
                dict(metadata=blog.metadata, post=post),
                os.path.join(output, '{}.html'.format(post.slug)))
    for asset in ['css', 'js']:
        if os.path.exists(os.path.join(output, asset)):
            shutil.rmtree(os.path.join(output, asset))
        shutil.copytree(os.path.join(theme, asset),
                        os.path.join(output, asset))
