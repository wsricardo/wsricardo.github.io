# Configuração do Pelican para wsricardo.github.io (v3)
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

AUTHOR = 'Wandeson Ricardo'
SITENAME = 'WSRicardo'
SITEURL = 'https://www.wsricardo.com.br'

PATH = 'content'
TIMEZONE = 'America/Sao_Paulo'
DEFAULT_LANG = 'pt-BR'

# URL Settings & Structure
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
CATEGORY_URL = '{slug}.html'
CATEGORY_SAVE_AS = '{slug}.html'

# Categories from specv3.md
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'Blog'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Links no Footer (conforme specv3.md)
LINKS = (
    ('Blog Antigo', 'https://wsricardo.blogspot.com'),
    ('GitHub', 'https://github.com/wsricardo'),
)

DEFAULT_PAGINATION = 10
RELATIVE_URLS = True
