#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'WouterDX'
SITENAME = 'Jupyter tricks'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en' #crashes if not in translation and diffrent fromt I18N settings.

IGNORE_FILES = ['.ipynb'] #does not help

# Pelican theme setup
THEME = 'pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'
#THEME = 'greizgh/pelican-material' #needs more plugins first

# JAVASCRIPT 
CUSTOM_CSS = 'static/css/custom.css'
CUSTOM_JS = 'static/js/custom.js'

STATIC_PATHS = ['extra']
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/css/custom.css'},
	'extra/custom.js': {'path': 'static/css/custom.js'}
	}
	

# PLUGINS
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = [
	'i18n_subsites',
	'series',
	'tag_cloud',
    'liquid_tags.youtube',
    'liquid_tags.notebook',
    'liquid_tags.include_code',
    'render_math',
    'pelican-ipynb.markup',
    'tipue_search']

# I18N CONFIG
#I18N_TEMPLATES_LANG = 'nl' #dutch language code
I18N_TEMPLATES_LANG = 'en' #same as default language code

# TIPUE SEARCH CONFIG
DIRECT_TEMPLATES = ('index','tags', 'categories', 'authors', 'archives', 'search')

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
