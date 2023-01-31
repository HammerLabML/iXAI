# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

from sphinx.builders.html import StandaloneHTMLBuilder
import os
import sys
sys.path.insert(0, os.path.abspath("../.."))
import ixai

# -- Project information ---------------------------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
project = 'ixai'
copyright = '2022, Maximilian Muschalik, Fabian Fumagalli, Rohit Jagtani'
author = 'Maximilian Muschalik, Fabian Fumagalli, Rohit Jagtani'
release = ixai.__version__
version = ixai.__version__

# -- General configuration -------------------------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
extensions = [
    "sphinx.ext.duration",
    "myst_parser",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.autosummary",
    'sphinx_copybutton',
    "sphinx.ext.viewcode",
    "sphinx.ext.autosectionlabel",
    "sphinx_autodoc_typehints",
    "sphinx_toolbox.more_autodoc.autoprotocol",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

intersphinx_mapping = {
    "python3": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
}

# -- Options for HTML output -----------------------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = 'furo'
html_static_path = ['_static']
#pygments_style = "sphinx"
pygments_dark_style = "monokai"
html_theme_options = {}

# -- Autodoc ---------------------------------------------------------------------------------------
autodoc_default_options = {
    'show-inheritance': False,
    'members': True,
    'member-order': 'groupwise',
    'special-members': '__call__',
    'undoc-members': True,
    'exclude-members': '__weakref__'
}
autoclass_content = 'class'
autodoc_inherit_docstrings = False

# -- Images ----------------------------------------------------------------------------------------
StandaloneHTMLBuilder.supported_image_types = [
    "image/svg+xml", "image/gif", "image/png", "image/jpeg"
]
# -- Copy Paste Button -----------------------------------------------------------------------------
# Ignore >>> when copying code
copybutton_prompt_text = r">>> |\.\.\. "
copybutton_prompt_is_regexp = True