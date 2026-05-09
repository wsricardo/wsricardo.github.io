from datetime import datetime

# Configurações de Data
NOW = datetime.now().date().strftime('%d-%m-%y')
SECTION="matematica"
AUTHOR = 'Wandeson Ricardo (WSRicardo)'
SITENAME = 'WSRicardo - Matemática'
SITEURL = "https://www.wsricardo.com.br"
#SITEURL="http://localhost:8000"

PAGENAME_TITLE = "WSRicardo - Matemática"
PAGENAME_DESCRIPTION = "Minhas notações e materiais diversos em matemática."
PATH = "content/"
OUTPUT_PATH = '../matematica/' # Diretório de saída na raiz do projeto principal

TIMEZONE = 'America/Sao_Paulo'
DEFAULT_LANG = 'pt-br'

# Feed generation
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Estrutura de URLs para Matemática
ARTICLE_PATHS = ['posts', 'articles']
ARTICLE_URL = 'posts/{date:%Y}/{date:%d}-{date:%m}-{slug}.html'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%d}-{date:%m}-{slug}.html'

PAGE_PATHS = ['pages']
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

STATIC_PATHS = ['imagens', 'arquivos']

DEFAULT_PAGINATION = 10
THEME = "../theme-wsricardo/"

# Configurações de URL Relativa para desenvolvimento
RELATIVE_URLS = False
SITE_ROOT_URL = f'{SITEURL}'

print(f"SITEURL : {SITEURL}")
