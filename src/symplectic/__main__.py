import sys

from symplectic import render

local_orbifold = render.Blog(
    metadata=render.Metadata(
         title="Local Patches of an Orbifold Life",
         description="Some small, random musing about life in an interesting place.",
    ),
    posts=[
        render.Post(
            title="On the weather",
            slug='weather',
            date="September 13th, 2017",
            author="Moshe Zadka",
            contents="<div>blah blah</div><div>blah blah blah</div>",
        ),
        render.Post(
            title="On the climate",
            slug='climate',
            date="September 14th, 2017",
            author="Moshe Zadka",
            contents="<div>bloh bloh</div><div>bloh bloh bloh</div>",
        ),
    ],
)

render.render(local_orbifold, sys.argv[1])
