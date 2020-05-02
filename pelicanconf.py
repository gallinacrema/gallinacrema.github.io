#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Mfg'
SITENAME = 'Code, Data and Random Thoughts'
SITEURL = 'http://localhost:8000'
SITETITLE = 'Code, Data and Random Thoughts'
SITELOGO = SITEURL + "/images/centralplace.jpg"
PYGMENTS_STYLE = 'friendly'

ROBOTS = 'index, follow'

THEME = "/Users/mfg/projects/gallinacrema.github.io/pelican-themes/flex"
PATH = 'content'
TIMEZONE = 'Europe/Madrid'
PLUGIN_PATHS = ['/Users/mfg/projects/gallinacrema.github.io/pelican-plugins']
PLUGINS = ['category_order','render_math']

DEFAULT_LANG = 'en'

DATE_FORMATS = {
    'en': '%B %d, %Y',
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

SOCIAL = (('twitter', 'https://twitter.com/mfgrela'),)

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

LINKS = (("Stastistical Modeling, Causal Inference and Social Science", 'https://statmodeling.stat.columbia.edu/'),
("Marc F. Bellemare", "http://marcfbellemare.com/wordpress/"),)

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['images']

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True