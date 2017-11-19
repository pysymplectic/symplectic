from xml.etree import ElementTree as ET

def _generate_atom(blog):
    root = ET.Element('feed')    
    root.SubElement('id').text = blog.base
    root.SubElement('title').text = blog.title
    root.SubElement('subtitle').text = blog.description
    root.SubElement('link', rel='alternate', type='text/html',
                            href=blog.base)
    gen = root.SubElement('generator', uri='http://github.com/pysymplectic')
    gen.text = 'Symplectic'
    for post in blog.posts:
        entry = root.SubElement('entry')
        entry.SubElement(
