"""
Symplectic -- a static blog generation library
"""
from symplectic.posts import Metadata, Blog
from symplectic.render import render
from symplectic.feed import render_atom_feed

__all__ = ['render', 'Metadata', 'Blog', 'render_atom_feed']
