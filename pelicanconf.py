#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#AUTHOR = 'Eric Van Albert'
SITENAME = 'Radiance'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

INDEX_SAVE_AS = "blog.html"

THEME = "nest"
NEST_HEADER_LOGO = "images/logo.png"

NEST_INDEX_HEAD_TITLE = u'Radiance Blog'
NEST_INDEX_HEADER_TITLE = u'Radiance Blog'
NEST_INDEX_HEADER_SUBTITLE = u'Algebra, art, and software engineering'
NEST_INDEX_CONTENT_TITLE = u'Latest Posts'

DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (
  ('Home','/'),
  ('Download','https://github.com/zbanks/radiance/releases'),
  ('Blog','/blog.html'),
)
