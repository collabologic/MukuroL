"""
TreeNodeをParsedNodeに変換
- 先頭がテンプレート名と一致するなら、tmplに入れる
- 先頭がテンプレート名と一致しないなら、tmplはpとし行は結合し直してtextとする
- 二つ目以降の値は、
    - ":"区切りなら、左辺をキーとしたdictを作ってParamsに入れる
    - ":"を含まなければ、そのままキーとして、値はTrueとしてParamsに入れる
- 再帰的にchildrenを処理する
"""
from .basic_tmpls import basic_tmpls
class ParsedNode:
    def __init__(self, tmpl, params):
        self.tmpl = tmpl
        self.params = params
        self.children = []

    def __repr__(self):
        return f"ParsedNode(tmpl={self.tmpl}, params={self.params}, children={self.children})"
    
    def to_dict(self):
        return {
            "tmpl": self.tmpl,
            "params": self.params,
            "children": [child.to_dict() for child in self.children]  # 再帰的に辞書化
        }

class parser:
    def __init__(self, tree):
        self.tree = tree

    def parse(self):
        # ノードをParsedNodeに変換
        return self.parse_tree_node(self.tree)

    # TreeNodeをParsedNodeに変換する
    def parse_tree_node(self, node):
        tmpl = None
        params = {}
        # 先頭の要素がテンプレート名と一致するか確認
        if node.value[0] in basic_tmpls.keys():
            # テンプレート名が一致する場合、tmplに入れる
            tmpl = node.value[0]
            # 二つ目以降の要素を処理する
            for param in node.value[1:]:
                if ":" in param:
                    key, value = param.split(":", 1)
                    params[key] = value
                else:
                    params[param] = True
        else:
            # テンプレート名が一致しない場合、tmplはpとし行は結合し直してtextとする
            tmpl = "p"
            params["text"] = " ".join(node.value)
        
        # 子ノードを再帰的に処理する
        parsed_node = ParsedNode(tmpl, params)
        for child in node.children:
            parsed_node.children.append(self.parse_tree_node(child))
        return parsed_node