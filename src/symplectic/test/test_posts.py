import unittest

import attr

from symplectic import posts


class PostsTest(unittest.TestCase):

    def setUp(self):
        self.post = posts.Post(title='', slug='foo', date='2017-11-13 22:23',
                               author='', contents='')

    def test_post_date(self):
        self.assertEquals(self.post.formatted_date, 'Mon Nov 13 22:23:00 2017')

    def test_post_rel_link(self):
        self.assertEquals(self.post.rel_link, 'foo.html')

    def test_page_rel_link(self):
        dct = attr.asdict(self.post)
        dct.pop('date')
        page = posts.Page(**dct)
        self.assertEquals(page.rel_link, 'foo.html')
