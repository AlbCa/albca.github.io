AUTHOR = 'Alberto Carrera'
SITENAME = 'Geoexp'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'Italian'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'https://getpelican.com/'),
#         ('Python.org', 'https://www.python.org/'),
#         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

FIRST_NAME = 'Alberto Carrera'
#SITEDESCRIPTION = 'https://github.com/mc-buckets/brutalistpelican'

##### Aggiunte #https://sammirabyan.github.io/build-with-pelican.html
STATIC_PATHS = ['images', 'pdfs']

OUTPUT_PATH = 'output/'

THEME = 'themes/brutalist' #Flex, brutalist

# Host on GitHub
SITEURL = 'https://albca.github.io'
DOMAIN = SITEURL
FEED_DOMAIN = SITEURL
HTTPS = True

