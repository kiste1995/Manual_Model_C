# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Instructors Version'
# copyright = '2021, Graziella'
author = 'Zetabank'

release = '0.1.3'
version = '0.1.3'

# -- General configuration

extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
    'sphinxcontrib.images',
    'sphinxcontrib.youtube',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']


images_config = {
    'download': True,
}


# -- Options for HTML output
html_static_path = ['_static']
html_logo = "_static/logo.png"
html_title = "ZetaBank - Instructor Version"
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'analytics_id': 'UA-17821189-2',
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'logo_only': False,
}

def setup(app):
    app.add_css_file("css/toc_custom.css")
# -- Referencing
numfig = True

# -- Options for EPUB output
epub_show_urls = 'footnote'
