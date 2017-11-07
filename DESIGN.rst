Design Notes
============

* There are three page types: "river" (the typical front page of a blog),
  "post" (also used for pages), the first post,
  and "list", a type of page with just links, no previews
  (e.g., that would be used for archives, by-tag, by-author)
* There will be decent default river.html/post.html/list.html that use
  METAL to take an "abstract.html" and specialize it
  (that should be good enough for the typical "bootstrap theme").
* No configuration file, no main. Usage will be documented as a library.
* Assets are just copied. Integration with asset pipelines is up to users of
  the library.
  
Imagined API:

.. code::

    import glob

    import symplectic
    from symplectic import jsonformat, rest

    METADATA = symplectic.Metadata(
        title="Local Patches of an Orbifold Life",
        description="Some small, random musing about life in an interesting "
                    "place.",
        links=[("GitHub", "https://github.com/moshez")],
    )

    POSTS = jsonformat.posts_from_json_files(glob.glob('*.json'))
    POSTS += rest.posts_from_rest_files(glob.glob('*.rst'))
    POSTS.sort(key=lambda post: post.date, reverse=True)
    PAGES = jsonformat.pages_from_json_files(glob.glob('pages/*.json'))
    PAGES += rest.pages_from_rest_files(glob.glob('pages/*.rst'))
    BLOG = symplectic.Blog(metadata=METADATA, posts=POSTS, pages=PAGES)
    symplectic.render(BLOG,
                      theme=['../../themes/basic', '../../themes/bs4blog'],
                      output='../../build/blog')
