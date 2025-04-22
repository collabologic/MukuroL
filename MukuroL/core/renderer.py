"""
コンバート済みのParsedNodeを用いて、HTMLを生成する。
- tmplの値に対応するテンプレートを用いる
- パラメータをそのまま渡す
- childrenがいる場合は、childrenを再帰的2にレンダリングし、{{inner}}に入れる
"""
from .basic_tmpls import basic_tmpls
from jinja2 import Template

class Renderer:
    def __init__(self, node):
        self.node = node

    def render(self):
        # tmplに対応するテンプレートを取得
        tmpl = basic_tmpls[self.node.tmpl]
        # jinja2のテンプレートを生成
        template = Template(tmpl)
        # paramsをそのまま渡す
        params = self.node.params.copy()
        # childrenがいる場合は、childrenを再帰的にレンダリングし、{{inner}}に入れる
        if self.node.children:
            inner_list = []
            for child in self.node.children:
                rendered_child = Renderer(child).render()
                if isinstance(rendered_child, str):
                    inner_list.append(rendered_child)
                else:
                    # エラー処理：文字列以外の場合はスキップするか、エラーログを出力する
                    print(f"Warning: child render result is not a string: {type(rendered_child)}")
            inner = "".join(inner_list)
            params["inner"] = inner
        
        return template.render({"data":params})