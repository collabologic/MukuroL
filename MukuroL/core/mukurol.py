from jinja2 import Template
from . import basic_tmpls
from .tokenizer import parse_indented_text
from .parser import parser
from .converter import convert
from .renderer import Renderer

class MukuroL:
    def __init__(self, templates=None, methods=None):
        self.templates = templates or {}
        self.methods = methods or {}
        self.add_templates(basic_tmpls.basic_tmpls)
        self.add_methods(basic_tmpls.basic_methods)

    def add_templates(self, templates):
        self.templates.update(templates)

    def add_methods(self, methods):
        self.methods.update(methods)

    def generate_html(self, mukurol_text):
        tree = parse_indented_text(mukurol_text)
        page = tree.children[0]
        # レイアウトHTMLの生成
        p = parser(page)
        parsed = p.parse()
        converted = convert(parsed)
        r = Renderer(converted)
        rendered = r.render()
        lines = [line for line in rendered.splitlines() if line.strip()]
        layout =  "\n".join(lines)

        return layout

