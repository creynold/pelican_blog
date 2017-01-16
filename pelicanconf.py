#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
#from markdown.extensions.toc import TocExtension
#from markdown.extensions.codehilite import CodeHiliteExtension

AUTHOR = u'Collin Reynolds'
SITENAME = u'Collin Mack'
SITEURL = ''

THEME='nest'
SITESUBTITLE=u'A Former Physicist Does Engineering'

NEST_HEADER_IMAGES = 'cayuga.jpg'
MENUITEMS = [('Home', '/'),]
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}
# index.html
NEST_INDEX_HEAD_TITLE = 'Home'
NEST_INDEX_HEADER_TITLE = u'Collin Reynolds - A Blog'
NEST_INDEX_HEADER_SUBTITLE = u'A Former Physicist Does Engineering'
NEST_INDEX_CONTENT_TITLE = u'Last Posts'

PATH = 'content'
OUTPUT_PATH = '../../collinmack_blog/'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         )

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
#Static files
STATIC_PATHS = ['images', 'extra/logo.svg']
PLUGIN_PATHS = ['plugins']
PLUGINS = ['render_math']
EXTRA_PATH_METADATA = {
    'extra/logo.svg': {'path': 'logo.svg'}
}
