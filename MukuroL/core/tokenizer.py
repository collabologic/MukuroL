"""
テキストを分解し、ツリー構造のNode配列とする。
各行は、トリミングした上で、半角スペースで配列とする
"""
from pprint import pprint
import json
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def __repr__(self):
        return f"TreeNode({self.value}, {self.children})"
    def to_dict(self):
        return {
            "value": self.value,
            "children": [child.to_dict() for child in self.children]  # 再帰的に辞書化
        }

def parse_indented_text(text):
    lines = text.split("\n")
    root = TreeNode("root")
    stack = [(0, root)]  # (indent_level, node)
    current = root
    for line in lines:
        stripped = line.lstrip()
        if not stripped:
            continue  # 空行をスキップ
        indent_level = len(line) - len(stripped)
        elements = stripped.split(" ")

        new_node = TreeNode(elements)
        # インデントレベルに応じて親を決定
        if indent_level == 0:
            current = root
        else :
            while stack and stack[-1][0] >= indent_level:
                stack.pop()
                current = stack[-1][1]
        
        if stack:
            stack.append((indent_level,new_node))
            current.children.append(new_node)
            current = new_node

        stack.append((indent_level, new_node))
    return root