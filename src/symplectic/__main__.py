import sys

from symplectic import render, parse

blog = parse.parse(sys.argv[3])
render.render(blog, sys.argv[1], sys.argv[2])
