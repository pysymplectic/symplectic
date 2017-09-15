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

    generate_website()