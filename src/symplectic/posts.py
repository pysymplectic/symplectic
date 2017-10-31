import datetime

import attr

@attr.s(frozen=True)
class Post(object):
    title = attr.ib()
    slug = attr.ib()
    date = attr.ib()
    author = attr.ib()
    contents = attr.ib()

    @property
    def formatted_date(self):
        when = datetime.datetime.strptime(self.date, "%Y-%m-%d %H:%M")
        return when.strftime('%c')

    @property
    def rel_link(self):
        return self.slug + '.html'

@attr.s(frozen=True)
class Page(object):
    title = attr.ib()
    slug = attr.ib()
    author = attr.ib()
    contents = attr.ib()

    formatted_date = ""

    @property
    def rel_link(self):
        return self.slug + '.html'

@attr.s(frozen=True)
class Metadata(object):
    title = attr.ib()
    description = attr.ib()
    links = attr.ib(default=attr.Factory(list))

@attr.s(frozen=True)
class Blog(object):
    metadata = attr.ib()
    posts = attr.ib()
    pages = attr.ib()
