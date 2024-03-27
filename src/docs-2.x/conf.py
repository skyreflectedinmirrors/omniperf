# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import subprocess as sp

sys.path.insert(0, os.path.abspath(".."))

repo_version = "unknown"
# Determine short version by file in repo
if os.path.isfile("../../VERSION"):
    with open("../../VERSION") as f:
        repo_version = f.readline().strip()


def install(package):
    sp.call([sys.executable, "-m", "pip", "install", package])


# -- Project information -----------------------------------------------------

project = "Omniperf"
copyright = "2023-2024, Advanced Micro Devices, Inc. All Rights Reserved"
author = "AMD Research"

# The short X.Y version
version = repo_version
# The full version, including alpha/beta/rc tags
release = repo_version

# -- General configuration ---------------------------------------------------

install("sphinx_rtd_theme")

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.githubpages",
    "myst_parser",
    "sphinxmark",
]

show_authors = True


myst_heading_anchors = 4
# enable replacement of (tm) & friends
myst_enable_extensions = ["replacements", "dollarmath"]


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}

# sphinxmark_enable = True
# sphinxmark_image = "text"
# sphinxmark_text = "Release Candidate"
# sphinxmark_text_size = 80
# sphinxmark_div = "document"
# sphinxmark_fixed = False
# sphinxmark_text_rotation = 30
# sphinxmark_text_color = (128, 128, 128)
# sphinxmark_text_spacing = 800
# sphinxmark_text_opacity = 30

from recommonmark.parser import CommonMarkParser

source_parsers = {".md": CommonMarkParser}

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None

# options for latex output
latex_engine = "lualatex"
latex_show_urls = "footnote"


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

latex_elements = {
    "sphinxsetup": "verbatimwrapslines=true, verbatimforcewraps=true",
}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "Omniperfdoc"

html_logo = 'images/amd-header-logo.svg'
html_theme_options = {
    "analytics_id": "G-C5DYLCE9ED",  #  Provided by Google in your dashboard
    "analytics_anonymize_ip": False,
    "logo_only": False,
    "display_version": True,
    "prev_next_buttons_location": "bottom",
    "style_external_links": False,
    "vcs_pageview_mode": "",
    # 'style_nav_header_background': 'white',
    # Toc options
    "collapse_navigation": True,
    "sticky_navigation": True,
    "navigation_depth": 5,
    "includehidden": True,
    "titles_only": False,
}

from pygments.styles import get_all_styles

# The name of the Pygments (syntax highlighting) style to use.
styles = list(get_all_styles())
preferences = ("emacs", "pastie", "colorful")
for pref in preferences:
    if pref in styles:
        pygments_style = pref
        break

from recommonmark.transform import AutoStructify


# app setup hook
def setup(app):
    app.add_config_value(
        "recommonmark_config",
        {
            "auto_toc_tree_section": "Contents",
            "enable_eval_rst": True,
            "enable_auto_doc_ref": False,
        },
        True,
    )
    app.add_transform(AutoStructify)
    app.add_config_value("docstring_replacements", {}, True)
    app.connect("source-read", replaceString)
    app.add_css_file("css/custom.css")


# function to replace version string througout documentation


def replaceString(app, docname, source):
    result = source[0]
    for key in app.config.docstring_replacements:
        result = result.replace(key, app.config.docstring_replacements[key])
    source[0] = result


docstring_replacements = {"{__VERSION__}": version}
