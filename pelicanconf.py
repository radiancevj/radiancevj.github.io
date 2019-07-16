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
NEST_HEADER_LOGO = "/images/logo.png"

NEST_INDEX_HEAD_TITLE = 'Radiance Blog'
NEST_INDEX_HEADER_TITLE = 'Radiance Blog'
NEST_INDEX_HEADER_SUBTITLE = 'Algebra, art, and software engineering'
NEST_INDEX_CONTENT_TITLE = 'Latest Posts'
NEST_HEADER_IMAGES = 'soupy_grid.jpg'

DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (
  ('Home','/'),
  ('Download','https://github.com/zbanks/radiance/releases'),
  ('Github','https://github.com/zbanks/radiance'),
  #('Blog','/blog.html'),
)

STATIC_PATHS = (
    'videos/',
    'images/',
    'android-chrome-192x192.png',
    'android-chrome-512x512.png',
    'apple-touch-icon.png',
    'browserconfig.xml',
    'favicon-16x16.png',
    'favicon-32x32.png',
    'favicon.ico',
    'mstile-150x150.png',
    'safari-pinned-tab.svg',
    'site.webmanifest',
)
