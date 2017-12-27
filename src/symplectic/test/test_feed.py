import os
import shutil
import tempfile
import unittest

from xml.etree import ElementTree as ET

import attr

import symplectic

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
        raise ValueError(feed_parsed)
