import os
import shutil

import chameleon

def _process(template, inputs, output_file):
    rendered = template(**inputs)
    with open(output_file, 'w') as fp:
        fp.write(rendered)

def render(blog, theme, output):
    if not os.path.exists(output):
        os.makedirs(output)
    loader = chameleon.PageTemplateLoader(theme)
    _process(loader['river.html'],
             dict(metadata=blog.metadata, posts=blog.posts,
                  archives=[dict(name='All', link='list.html')]),
             os.path.join(output, 'river.html'))
    _process(loader['list.html'],
             dict(metadata=blog.metadata, posts=blog.posts,
                  archives=[dict(name='All', link='list.html')]),
             os.path.join(output, 'list.html'))
    for i, post in enumerate(blog.posts):
        _process(loader['post.html'],
                 dict(metadata=blog.metadata, post=post),
                 os.path.join(output, '{}.html'.format(post.slug)))
    for asset in ['css', 'js']:
        if os.path.exists(os.path.join(output, asset)):
            shutil.rmtree(os.path.join(output, asset))
        shutil.copytree(os.path.join(theme, asset),
                        os.path.join(output, asset))
