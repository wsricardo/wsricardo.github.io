from datetime import datetime

#NOW = datetime.now().date().isoformat()
NOW = datetime.now().date().strftime( '%d-%m-%y ')

AUTHOR = 'Wandeson Ricardo (WSRicardo)'
SITENAME = 'WSRicardo Blog'
SITEURL = "https://www.wsricardo.com.br"

SECTION = "blog"

PAGENAME_TITLE = "WSRicardo Blog"
PAGENAME_DESCRIPTION = "Minhas notações e materiais diversos."


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

# --- Estrutura de URL para o Blog ---
ARTICLE_PATHS = [ 'posts', 'articles' ]
ARTICLE_URL = 'blog/posts/{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = 'blog/posts/{date:%Y}/{date:%m}/{slug}.html'

PAGE_PATHS = ['pages']
PAGE_URL = 'blog/pages/{slug}.html'
PAGE_SAVE_AS = 'blog/pages/{slug}.html'

CATEGORY_URL = 'blog/category/{slug}.html'
CATEGORY_SAVE_AS = 'blog/category/{slug}.html'
TAG_URL = 'blog/tag/{slug}.html'
TAG_SAVE_AS = 'blog/tag/{slug}.html'
AUTHOR_URL = 'blog/author/{slug}.html'
AUTHOR_SAVE_AS = 'blog/author/{slug}.html'

STATIC_PATHS = ['imagens' , 'arquivos']
OUTPUT_PATH = 'blog/'
SITE_ROOT_URL = f'{ SITEURL }' # Variável para a raiz do site em desenvolvimento
