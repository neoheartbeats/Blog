import alabaster

### Project properties
project = 'Scheilya ME'
copyright = '2022, Ilya.w'
author = 'Ilya.w'

### General configurations
extensions = ['alabaster']
templates_path = ['_templates']
exclude_patterns = []

### `HTML' output configurations
## `CSS' related settings
html_theme = 'alabaster'
html_theme_path = [alabaster.get_path()]
html_static_path = ['_static']
html_theme_options = {
    'description': "SCHEilya.ME",
    'logo': 'logo.png',
    'fixed_sidebar': 'true',
    'show_related': 'true',
    'show_powered_by': 'false',
    'touch_icon': 'logo.png',
    'base_bg': "#000000",
    'base_text': "#dddddd",
    'hr_border': "#dddddd",
    'body_bg': "#000000",
    'body_text': "#dddddd",
    'shadow' : "#000000",
    'link': "#6ae4b9",
    'link_hover': "#f78fe7",
    'sidebar_header': "#f78fe7",
    'sidebar_text': "#dddddd",
    'sidebar_link': "#6ae4b9",
    'code_bg': "#000000",
    'code_text': "#00c06f",
    'code_hover': "#323232",
    'code_highlight': "#00c06f",
    'code_font_family': "Fira Code",
    'font_family': "Fira Sans",
    'head_font_family': "Fira Sans Bold",
    'caption_font_family': "Fira Sans"
}

## Site identity settings
html_favicon = None

# Text
html_title = 'SCHEilya.ME'

## Source file names
root_doc = 'index'
source_suffix = '.rst'

## Ignored source files
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

def setup(app):
    app.add_css_file('styles.css')