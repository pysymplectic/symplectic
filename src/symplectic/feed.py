from xml.etree import ElementTree as ET

def to_timestamp(dt_obj):
    dt_obj = dt_obj.astimezone(UTC)
    return dt_obj.strftime('%Y-%m-%dT%H:%M:%SZ')

def _generate_atom(blog, fp):
    root = ET.Element('feed',
                      xmlns="http://www.w3.org/2005/Atom")
    ET.SubElement(root, 'id').text = blog.metadata.base
    ET.SubElement(root, 'title').text = blog.metadata.title
    ET.SubElement(root, 'subtitle').text = blog.metadata.description
    ET.SubElement(root, 'updated').text = to_timestamp(datetime.datetime.now())
    ET.SubElement(root, 'link', rel='alternate', type='text/html',
                                href=blog.metadata.base)
    gen = ET.SubElement(root, 'generator', uri='http://github.com/pysymplectic')
    gen.text = 'Symplectic'
    for post in blog.posts:
        entry = ET.SubElement(root, 'entry')
        abs_url = blog.metadata.base + '/' + post.rel_link
        ET.SubElement(entry, 'id').text = abs_url
        ET.SubElement(ET.SubElement(entry, 'author'), 'name').text = post.author
        ET.SubElement(entry, 'title').text = post.title
        ET.SubElement(entry, 'link', rel='alternate', type='text/html',
                         href=abs_url)
        ET.SubElement(entry, 'published').text = post.date
        content = '<div>{}</div>'.format(post.contents)
        ET.SubElement(entry, 'context', type='html').append(ET.fromstring(content))
    ET.ElementTree(root).write(fp)
