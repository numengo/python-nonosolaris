SIMPLE_SETTINGS = {
    'OVERRIDE_BY_ENV': True,
    'CONFIGURE_LOGGING': True,
    'DYNAMIC_SETTINGS': {
        'backend': 'redis',
        'pattern': 'DYNAMIC_*',
        'auto_casting': True,
        'prefix': 'NONOSOLARIS_'
    }
}

DEFAULT_CONTEXT = {
    'cell_id': 'Ma Cellule Solaris',
    'cell': {
    }
}

# config settings
CLI_CONTEXT_FILENAME = 'solaris.nono'
SOLARIS_DIR = '~/Solaris'

# directories
MEMBER_DIRNAME = 'fiches'
BUILD_DIRNAME = 'build'
PAGES_DIRNAME = 'pages'
FORMS_DIRNAME = 'forms'

# templates
FORM_PAGE = 'templates/formulaire_annuaire_v1.0.pdf'
COVER_PAGE = 'templates/cover_annuaire_v1.0.pdf'
ADDR_BOOK_PAGE = 'templates/page_annuaire_v1.0.pdf'
ADDR_BOOK_PREFIX = 'annuaire-solaris'

# layout
INDEX_TITLE_SPACE = 40
TOC_SPACE = 25
INDEX_MARGIN = 20
