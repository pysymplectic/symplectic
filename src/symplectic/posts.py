import attr

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
