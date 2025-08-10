from datetime import datetime

#NOW = datetime.now().date().isoformat()
NOW = datetime.now().date().strftime( '%d-%m-%y ')

AUTHOR = 'Wandeson Ricardo (WSRicardo)'
SITENAME = 'WSRicardo Blog'
SITEURL = ""

PATH = "content/posts"

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10
THEME = "theme"

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
ARTICLE_PATHS = 'posts/'
ARTICLE_URL = 'posts/{date:%Y}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{slug}/index.html'

PAGE_PATHS = 'pages/'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
STATIC_PATHS = ['images' , 'arquivos']
OUTPUT_PATH = 'blog/'


