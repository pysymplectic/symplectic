import tempfile
import unittest

from symplectic import rest


class JSONFormatTest(unittest.TestCase):

    def test_parse_post(self):
        with tempfile.NamedTemporaryFile() as fp:
            fp.write("""
stuff
=====

:slug: things
:date: 2017-09-17 22:22
:author: Foo Bar

things sure are stuff
            """.encode('utf-8'))
            fp.flush()
            res, = rest.posts_from_rest_files([fp.name])
        self.assertEquals(res.title, 'stuff')
        self.assertEquals(res.author, 'Foo Bar')

    def test_parse_page(self):
        with tempfile.NamedTemporaryFile() as fp:
            fp.write("""
stuff
=====

:slug: things
:author: Foo Bar

things sure are stuff
            """.encode('utf-8'))
            fp.flush()
            res, = rest.pages_from_rest_files([fp.name])
        self.assertEquals(res.title, 'stuff')
        self.assertEquals(res.author, 'Foo Bar')
