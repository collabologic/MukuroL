from core.mukurol import MukuroL

text = """\
parts
    greeting 
        box label:greeting text:こんにちは
            本日は良い天気ですね
            明日は雨だそうです。
    farewell
        box label:farewell text:さようなら
            また明日お会いしましょう
page text:サンプルページ
    grid size:full tile:10x10
        box label:Header gsize:10x2 text:ここにヘッダーが入ります
        box label:Sidebar gsize:3x7 text:サイドバー。メニューなど
        box label:Body gsize:7x7 text:本文。メインコンテンツ
            flex size:full direction:column
                box label:Form text:ここに入力フォームが入ります
                    フォームは部品をテンプレート化した方が良いかもしれません
                box label:Preview text:入力結果がプレビューされます
            ref greeting
            ref farewell
        box label:Footer gsize:10x1 text:フッターです
"""
# Example usage:
if __name__ == '__main__':
    # Create an instance of the HTMLGenerator
    generator = MukuroL()

    # Generate HTML using the templates and data
    html_output = generator.generate_html(text)
    print(html_output)