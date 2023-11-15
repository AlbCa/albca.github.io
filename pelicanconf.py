AUTHOR = 'Alberto Carrera'
SITENAME = 'Geoexp'
SITEURL = ''

# Categories
USE_FOLDER_AS_CATEGORY = True
DISPLAY_CATEGORIES_ON_MENU = True

# Pages
DISPLAY_PAGES_ON_MENU = False

PATH = 'content'
STATIC_PATHS = ['images', 'pdfs']
TIMEZONE = 'Europe/Berlin'
DEFAULT_LANG = 'en'
#OUTPUT_PATH = 'output'
DEFAULT_PAGINATION = 4

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Theme Settings
THEME = 'themes/brutalist'
#SITEIMAGE = 'site-cover.jpg'
#SITEDESCRIPTION = 'A simple, accessible, content-first Pelican theme inspired by David Bryant Copeland\'s https://brutalist-web.design/'
## path to logo for nav menu (optional)
LOGO = 'aclogo.png'
## first name for nav menu if logo isn't provided
FIRST_NAME = 'Geoexp - Alberto Carrera'
## Toggle display of theme attribution in the footer (scroll down and see)
## Attribution is appreciated but totally fine to turn off!
#ATTRIBUTION = True

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)
STRAVA = 'https://www.strava.com/athletes/50890324'
GITHUB = 'https://github.com/AlbCa/'
INSTAGRAM = 'https://www.instagram.com/_herbee/'

# PLUGINS
PLUGIN_PATHS = ['plugins']
PLUGINS = ['sitemap', 'optimize_images', 'gzip_cache']

## SITEMAP PLUGIN
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': .99,
        'pages': .75,
        'indexes': .5
    },
    'changefreqs': {
        'articles': 'daily',
        'pages': 'daily',
        'indexes': 'daily'
    },
}

MENUITEMS = [
    ('geophysics', '/pages/geophysics.html'),
    ('outdoor', '/pages/outdoor.html'),
    ('publications', '/pages/publications.html'),
    ('contact', '/pages/contact.html'),
    ]

# Host on GitHub
#SITEURL = 'https://albca.github.io'
#DOMAIN = SITEURL
#FEED_DOMAIN = SITEURL
#HTTPS = True

# Blogroll
#LINKS = (('Pelican', 'https://getpelican.com/'),
#         ('Python.org', 'https://www.python.org/'),
#         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#         ('You can modify those links in your config file', '#'),)




