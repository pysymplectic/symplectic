import tempfile
import unittest

from symplectic import jsonformat

class JSONFormatTest(unittest.TestCase):

    def test_parse(self):
        with tempfile.NamedTemporaryFile() as fp:
            fp.write("""
            {
            "title": "things",
            "slug": "stuff",
            "date": "2017-09-14 22:21",
            "author": "Foo Bar",
            "contents": "stuff sure are things"
            }
            """.encode('utf-8'))
            fp.flush()
            res, = jsonformat.posts_from_json_files([fp.name])
        self.assertEquals(res.title, 'things')
