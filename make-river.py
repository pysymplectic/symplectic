import os
import shutil

import chameleon

def process(template_file, inputs):
    with open(template_file) as fp:
        template_str = fp.read()
    template = chameleon.PageTemplate(template_str)
    with open(os.path.join('build', template_file), 'w') as fp:
        fp.write(template(**inputs))

river_inputs = dict(
    title="Local Patches of an Orbifold Life",
    description="Some small, random musing about life in an interesting place.",
    posts=[
        dict(title="On the weather",
             date="September 13th, 2017",
             author="Moshe Zadka",
             preview="<div>blah blah</div>",
             )
    ],
)

post_inputs = dict(
    title="Local Patches of an Orbifold Life",
    description="Some small, random musing about life in an interesting place.",
    post=dict(title="On the weather",
             date="September 13th, 2017",
             author="Moshe Zadka",
             contents="<div>blah blah</div><div>blah blah blah</div>",
             ),
)

process('river.html', river_inputs)
process('post.html', post_inputs)

for asset in ['css', 'js']:
    if os.path.exists(os.path.join('build', asset)):
        shutil.rmtree(os.path.join('build', asset))
    shutil.copytree(asset, os.path.join('build', asset))
