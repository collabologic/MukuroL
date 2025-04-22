"""
ParsedNodeに、関数処理を追加
- パラメータのdictのキーが、関数一覧と一致してた場合
    - 関数を実行して、パラメータ変換を行う
- 一致していなかった場合
    - そのままパラメータを使う
"""
from .basic_tmpls import basic_methods

class ConvertedNode:
    def __init__(self, tmpl):
        self.tmpl = tmpl
        self.params = {}
        self.children = []

    def __repr__(self):
        return f"ConverteddNode(tmpl={self.tmpl}, params={self.params}, children={self.children})"
    
    def to_dict(self):
        return {
            "tmpl": self.tmpl,
            "params": self.params,
            "children": [child.to_dict() for child in self.children]  # 再帰的に辞書化
        }

def convert(parsedNode):

    # ConvertedNodeを生成
    convertedNode = ConvertedNode(parsedNode.tmpl)
    # パラメータのdictのキーが、関数一覧と一致してた場合
    for key in parsedNode.params.keys():
        method_name = f"{parsedNode.tmpl}_{key}"
        if method_name in basic_methods.keys():
            # 関数を実行して、params["style"]に書き足していく
            if "style" not in convertedNode.params:
                convertedNode.params["style"] = ""
            convertedNode.params["style"] += basic_methods[method_name](parsedNode.params[key])
        else:
            # 一致していなかった場合、そのままパラメータを使う
            convertedNode.params[key] = parsedNode.params[key]
    # 子ノードを再帰的に処理する
    for child in parsedNode.children:
        convertedNode.children.append(convert(child))
    return convertedNode
    