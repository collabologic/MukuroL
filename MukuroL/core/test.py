# 以下はテスト
import json

from tokenizer import parse_indented_text
from parser import parser
from converter import convert
from renderer import Renderer

text = """\
page text:サンプルページ
    grid size:full tile:10x10
        box label:Header gsize:10x2 text:ここにヘッダーが入ります
        box label:Sidebar gsize:3x7 text:サイドバー。メニューなど
        box label:Body gsize:7x7 text:本文。メインコンテンツ
            flex size:full direction:column
                box label:Form text:ここに入力フォームが入ります
                    フォームは部品をテンプレート化した方が良いかもしれません
                box label:Preview text:入力結果がプレビューされます
        box label:Footer gsize:10x1 text:フッターです
"""

tree = parse_indented_text(text)
stack_json = json.dumps(
    tree.to_dict(),
    ensure_ascii=False, indent=4
)
#print(stack_json)

page = None
print(json.dumps(
    ensure_ascii=False, indent=4
))

print("linking")
linked_page = None
print(json.dumps(
    linked_page.to_dict(),
    ensure_ascii=False, indent=4
))

print("parsed")
p = parser(linked_page)
parsed = p.parse()
print(json.dumps(
    parsed.to_dict(),
    ensure_ascii=False, indent=4
))
print("converted")
converted = convert(parsed)
print(json.dumps(
    converted.to_dict(),
    ensure_ascii=False, indent=4
))

print("rendered")
r = Renderer(converted)
rendered = r.render()
print(rendered)
print("done")