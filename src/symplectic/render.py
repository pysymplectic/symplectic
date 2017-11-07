import functools
import os
import shutil

import chameleon

def _process(template, inputs, output_file):
    rendered = template(**inputs)
    with open(output_file, 'w') as fp:
        fp.write(rendered)

def _dict_sum(d1, **d2):
    ret = d1.copy()
    ret.update(d2)
    return ret

def render(blog, theme, output):
    if not os.path.exists(output):
        os.makedirs(output)
    loader = chameleon.PageTemplateLoader(theme)
    base_dict = dict(metadata=blog.metadata, pages=blog.pages,
                     pagination=None,
                     archives=[dict(name='All', link='list.html')])
    regular_and = functools.partial(_dict_sum, base_dict)
    _process(loader['river.html'],
             regular_and(posts=blog.posts),
             os.path.join(output, 'river.html'))
    _process(loader['list.html'],
             regular_and(posts=blog.posts),
             os.path.join(output, 'list.html'))
    for post in blog.posts:
        _process(loader['post.html'],
                 regular_and(post=post),
                 os.path.join(output, '{}.html'.format(post.slug)))
    for page in blog.pages:
        _process(loader['post.html'],
                 regular_and(post=page),
                 os.path.join(output, '{}.html'.format(page.slug)))
    if isinstance(theme, list):
        dname = theme[-1]
    else:
        dname = theme
    for asset in ['css', 'js']:
        if os.path.exists(os.path.join(output, asset)):
            shutil.rmtree(os.path.join(output, asset))
        shutil.copytree(os.path.join(dname, asset),
                        os.path.join(output, asset))
