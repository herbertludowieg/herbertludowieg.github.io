# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Personal Website'
copyright = '2023, Herbert Daniel Ludowieg'
author = 'Herbert Daniel Ludowieg'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.mathjax',
    'myst_parser',
    'sphinx_design',
    'nbsphinx',
]

myst_enable_extensions = [
    "amsmath",
    "dollarmath",
]
myst_dmath_allow_labels=True

source_suffix = ['.rst', '.md']

master_doc = 'index'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_theme_options = {
    "home_page_in_toc": True,
    "show_navbar_depth": 3,
    "icon_links": [
        {
            "name": "LinkedIn",
            "url": "https://www.linkedin.com/in/herbert-daniel-ludowieg-442ba2a0/",
            "icon": "fa-brands fa-linkedin",
            "type": "fontawesome"
        },
        {
            "name": "GitHub",
            "url": "https://github.com/herbertludowieg",
            "icon": "fa-brands fa-github",
            "type": "fontawesome"
        },
        {
            "name": "Resume",
            "url": "_static/Herbert_Ludowieg_Resume.pdf",
            "icon": "fa-solid fa-download",
            "type": "fontawesome"
        },
        {
            "name": "ORCiD",
            "url": "https://orcid.org/0000-0002-4786-1348",
            "icon": "fa-brands fa-orcid",
            "type": "fontawesome"
        },
        {
            "name": "Google Scholar",
            "url": "https://scholar.google.com/citations?user=4pxDwJIAAAAJ&hl",
            "icon": "fa-brands fa-google-scholar",
            "type": "fontawesome"
        },
    ],
}

html_title = "Herbert D. Ludowieg"

html_logo = "assets/img/phd-with-bull-crop.jpg"

#togglebutton_hint = "Show More"
#togglebutton_hint_hide = "Show Less"
