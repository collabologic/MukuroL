"""
importディレクトリ部の処理 => 一旦見送り
"""
from pprint import pprint
def divide(root):
    """
    TreeNodeを受け取り、partsとpageとimportに分ける
    - pageはpageノードの子ノード
    """
    page = None
    for child in root.children:
        if child.value[0] == "page":
            #page = child.children
            page = [child]
        elif child.value[0] == "import":
            # importノードは無視する
            continue
        else:
            raise ValueError(f"Unknown node type: {child.value[0]}")
    return page[0] if page else None
