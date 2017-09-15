import chameleon

with open("river.html") as fp:
    river = fp.read()

template = chameleon.PageTemplate(river)

derived = dict(
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

with open("build/river.html", 'w') as fp:
    fp.write(template(**derived))
