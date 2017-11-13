import glob
import os
import shutil
import tempfile
import unittest

import symplectic
from symplectic import posts

class RenderTest(unittest.TestCase):

    def setUp(self):
        metadata = symplectic.Metadata(
                          title="A test",
                          description="Testing stuff",
                          links=[("Example", "https://example.com/test")],
                        )
        posts = []
        pages = []
        self.blog = symplectic.Blog(metadata=metadata, posts=posts, pages=pages)
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
          <li tal:repeat="page pages"><a href="#" tal:attributes="href page.rel_link" tal:content="page.title">About</a></li>
          </ul>
          <p tal:content="metadata.description">A description</p>
          <div metal:define-slot="main">
             This is where the main content goes.
          </div>
          <h4>Archives</h4>
          <ol>
          <li tal:repeat="archive archives"><a href="#" tal:attributes="href archive.link" tal:content="archive.name">March 2014</a></li>
          </ol>
          <h4>Elsewhere</h4>
          <ol>
          <li tal:repeat="link metadata.links"><a href="#" tal:attributes="href link[1]" tal:content="link[0]">GitHub</a></li>
          </ol>
          </body></html>""")

    def test_empty_render(self):
        symplectic.render(self.blog,
                          theme=[self.themedir],
                          output=self.blogdir)
        raise ValueError(glob.glob(self.blogdir + '/*'))
