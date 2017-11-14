import os
import shutil
import tempfile
import unittest

from xml.etree import ElementTree as ET

import attr

import symplectic
from symplectic import posts

NS = '{http://www.w3.org/1999/xhtml}'


class RenderTest(unittest.TestCase):

    def setUp(self):
        metadata = symplectic.Metadata(
                          title="A test",
                          description="Testing stuff",
                          links=[("Example", "https://example.com/test")],
                        )
        posts = []
        pages = []
        self.blog = symplectic.Blog(metadata=metadata,
                                    posts=posts, pages=pages)
        self.addCleanup(lambda: shutil.rmtree(self.blogdir))
        self.blogdir = tempfile.mkdtemp()
        self.addCleanup(lambda: shutil.rmtree(self.themedir))
        self.themedir = tempfile.mkdtemp()
        os.mkdir(os.path.join(self.themedir, 'css'))
        os.mkdir(os.path.join(self.themedir, 'js'))
        with open(os.path.join(self.themedir, 'master.html'), 'w') as fp:
            fp.write("""
            <!DOCTYPE html>
            <html xmlns="http://www.w3.org/1999/xhtml"
                  xmlns:tal="http://xml.zope.org/namespaces/tal"
                  xmlns:metal="http://xml.zope.org/namespaces/metal"
                  xmlns:i18n="http://xml.zope.org/namespaces/i18n"
                  define-macro="master">
              <head>
              <title tal:content="metadata.title">Blog Template Nineties Web</title>
              </head>
          <body>
          <h1><a tal:content="metadata.title" href="index.html">The Blog</a></h1>
          <p>My pages</p>
          <ul>
          <li tal:repeat="page pages">
          <a href="#" tal:attributes="href page.rel_link"
                      tal:content="page.title">About</a></li>
          </ul>
          <p tal:content="metadata.description">A description</p>
          <div metal:define-slot="main">
             This is where the main content goes.
          </div>
          <h4>Archives</h4>
          <ol>
          <li tal:repeat="archive archives">
           <a href="#" tal:attributes="href archive.link"
                       tal:content="archive.name">March 2014</a></li>
          </ol>
          <h4>Elsewhere</h4>
          <ol>
          <li tal:repeat="link metadata.links">
          <a href="#" tal:attributes="href link[1]"
                      tal:content="link[0]">GitHub</a></li>
          </ol>
          </body></html>""")

    def test_empty_render(self):
        symplectic.render(self.blog,
                          theme=[self.themedir],
                          output=os.path.join(self.blogdir, 'blog'))
        with open(os.path.join(self.blogdir, 'blog', 'river.html')) as fp:
            river = fp.read()
        river_parsed = ET.fromstring(river)
        title, = river_parsed.iter(NS + 'title')
        self.assertEquals(title.text, self.blog.metadata.title)
        archives, links = river_parsed.iter(NS + 'li')
        links, = links.iter(NS + 'a')
        self.assertEquals(links.text, self.blog.metadata.links[0][0])
        self.assertEquals(links.attrib,
                          dict(href=self.blog.metadata.links[0][1]))
        with open(os.path.join(self.blogdir, 'blog', 'list.html')) as fp:
            archives = fp.read()
        archives_parsed = ET.fromstring(archives)
        title, = archives_parsed.iter(NS + 'title')
        self.assertEquals(title.text, self.blog.metadata.title)

    def test_one_post_render(self):
        post = posts.Post(title='hey there', slug='foo',
                          date='2017-11-13 22:23',
                          author='', contents='')
        blog = attr.evolve(self.blog, posts=[post])
        symplectic.render(blog,
                          theme=[self.themedir],
                          output=os.path.join(self.blogdir))
        with open(os.path.join(self.blogdir, 'foo.html')) as fp:
            foo = fp.read()
        foo_parsed = ET.fromstring(foo)
        h2, = foo_parsed.iter(NS + 'h2')
        self.assertEquals(h2.text, post.title)

    def test_one_page_render(self):
        page = posts.Page(title='hey there', slug='foo',
                          author='', contents='')
        blog = attr.evolve(self.blog, pages=[page])
        symplectic.render(blog,
                          theme=[self.themedir],
                          output=os.path.join(self.blogdir))
        with open(os.path.join(self.blogdir, 'foo.html')) as fp:
            foo = fp.read()
        foo_parsed = ET.fromstring(foo)
        h2, = foo_parsed.iter(NS + 'h2')
        self.assertEquals(h2.text, page.title)

    def test_remove_css(self):
        with open(os.path.join(self.themedir, 'css', 'foo.css'), 'w') as fp:
            fp.write('haha')
        os.mkdir(os.path.join(self.blogdir, 'css'))
        with open(os.path.join(self.blogdir, 'css', 'foo.css'), 'w') as fp:
            fp.write('hoho')
        symplectic.render(self.blog,
                          theme=[self.themedir],
                          output=os.path.join(self.blogdir))
        with open(os.path.join(self.blogdir, 'css', 'foo.css')) as fp:
            foo = fp.read()
        self.assertEquals(foo, 'haha')
