import io

from xml.etree import ElementTree as ET

from docutils import core as ducore, io as duio
from docutils.writers import html4css1

from docutils.writers.html4css1 import HTMLTranslator, Writer

from symplectic import posts

def parse_docinfo(docinfo):
    parsed = ET.fromstring(docinfo)
    ret = {}
    for elem in parsed.find('tbody').findall('tr'):
        field = elem.find('th').text.strip(':').lower()
        value = elem.find('td').text
        ret[field] = value
    return ret

def pages_from_rest_files(fnames):
    overrides = {'input_encoding': 'utf-8',
                 'initial_header_level': 2}
    ret = []
    for fname in fnames:
        with io.open(fname, "r", encoding='utf-8') as fp:
            input_string = fp.read()
        parts = ducore.publish_parts(
            source=input_string, source_path=fname,
            writer_name='html', settings_overrides=overrides)
        docinfo = parse_docinfo(parts['docinfo'])
        page = posts.Page(title=parts['title'],
                          contents=parts['body'],
                          slug=docinfo['slug'],
                          author=docinfo['author'],
                         )
        ret.append(page)
    return ret
