import os
import shutil
import tempfile
import unittest

from xml.etree import ElementTree as ET

import attr

import symplectic
from symplectic import posts

NS = '{http://www.w3.org/2005/Atom}'


class FeedTest(unittest.TestCase):

    def setUp(self):
        metadata = symplectic.Metadata(
                          title="A test",
                          description="Testing stuff",
                          base="https://example.net",
                        )
        self.blog = symplectic.Blog(metadata=metadata,
                                    posts=[], pages=[])
        self.addCleanup(lambda: shutil.rmtree(self.blogdir))
        self.blogdir = tempfile.mkdtemp()

    def test_empty_render(self):
        symplectic.render_atom_feed(self.blog, output=self.blogdir)
        with open(os.path.join(self.blogdir, 'atom.xml')) as fp:
            feed = fp.read()
        feed_parsed = ET.fromstring(feed)
        self.assertEquals(feed_parsed.tag, NS + 'feed')
        title, = feed_parsed.iter(NS + 'title')
        self.assertEquals(title.text, 'A test')
        subtitle, = feed_parsed.iter(NS + 'subtitle')
        self.assertEquals(subtitle.text, 'Testing stuff')
        updated, = feed_parsed.iter(NS + 'updated')
        self.assertEquals(updated.text[:2], '20') # Test will fail in 80 years

    def test_one_render(self):
        post = posts.Post(title='hey there', slug='foo',
                          date='2017-11-13 22:23',
                          author='', contents='')
        blog = attr.evolve(self.blog, posts=[post])
        symplectic.render_atom_feed(blog, output=self.blogdir)
        with open(os.path.join(self.blogdir, 'atom.xml')) as fp:
            feed = fp.read()
        feed_parsed = ET.fromstring(feed)
        entry, = feed_parsed.iter(NS + 'entry')
        my_id, = entry.iter(NS + 'id')
        self.assertEquals(my_id.text, u'https://example.net/foo.html')
