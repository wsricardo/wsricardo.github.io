from datetime import datetime

#NOW = datetime.now().date().isoformat()
NOW = datetime.now().date().strftime( '%d-%m-%y ')

AUTHOR = 'Wandeson Ricardo (WSRicardo)'
SITENAME = 'WSRicardo Blog'
SITEURL = "http://localhost:5500"

print(f"SITEURL : {SITEURL  }")
PATH = "content/"

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt-br'

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
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
THEME = "theme-wsricardo/"

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False
ARTICLE_PATHS = [ 'posts', 'articles' ]
ARTICLE_URL = 'blog/posts/{date:%Y}/{date:%d}-{date:%m}-{slug}.html'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%d}-{date:%m}-{slug}.html'

PAGE_PATHS = ['pages']
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
STATIC_PATHS = ['imagens' , 'arquivos']
OUTPUT_PATH = 'blog/'
SITE_ROOT_URL = f'{ SITEURL }' # Variável para a raiz do site em desenvolvimento
