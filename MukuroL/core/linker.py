"""
importディレクトリ部の処理 => 一旦見送り
    指定ソースを取り込み、tokenizeした上でparts欄に追記し、import欄は削除する
TreeNodeに含まれるrefを処理する
    partsにはrefは使えない
    ref欄はparts内の記述に差し替える
"""
def divide(root):
    """
    TreeNodeを受け取り、partsとpageとimportに分ける
    - partsはpartsノードの子ノード
    - pageはpageノードの子ノード
    - importはimportノードの子ノード
    """
    parts = None
    page = None
    for child in root.children:
        if child.value[0] == "parts":
            parts = child.children
        elif child.value[0] == "page":
            #page = child.children
            page = [child]
        elif child.value[0] == "import":
            # importノードは無視する
            continue
        else:
            raise ValueError(f"Unknown node type: {child.value[0]}")
    return parts, page[0] if page else None

def linking(current, parts): 
    # refノードであった場合、partsディレクティブ内からキーに対応するパーツを探す
    if current.value[0] == "ref":
        # partsノード内で、current.value[1]と一致するノードを探す
        ref = None
        for child in parts:
            if child.value[0] == current.value[1]:
                ref = child.children[0] if child.children else child
                break
        # refノードが見つからなければ、エラーを出す
        if ref is None:
            raise ValueError(f"refノードが見つかりません: {current.value[1]}")
        # refノードが見つかった場合、currentノードをrefノードに置き換える
        current = ref
    else:
        # ref以外は子ノードを再帰的に処理する
        for i in range(len(current.children)):
            current.children[i] = linking(current.children[i], parts)
    return current
