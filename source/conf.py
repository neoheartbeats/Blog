### Project properties
project = 'Scheilya ME'
copyright = '2022, Ilya.w'
author = 'Ilya.w'

### General configurations
extensions = []
templates_path = ['_templates']
exclude_patterns = []

### `HTML' output configurations
## `CSS' related settings 
html_theme = 'alabaster'
html_static_path = ['_static']

## Site identity settings
# Icons
html_logo = './docs/img/logo.png'
html_favicon = None

# Text
html_title = 'ILYA ME'

## Source file names
root_doc = 'index'
source_suffix = '.rst'

## Ignored source files
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

## Syntax highlighting style
pygments_style = 'sphinx'