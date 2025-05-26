basic_tmpls = {
    "page":"""\
<html>
  <header>
    {% if data.title %}<title>{{data.title}}</title>{% endif %}
    <link rel="stylesheet" href="style.css">
    <meta charset="UTF-8">
  </header>
  <body>
    {% if data.inner %}
        {{data.inner}}
    {% endif %}
  </body>
</html>
""",
    "box": """\
<div 
  {% if data.id %}id='{{data.id}}'{% endif %}
  class='box {% if data.class %}{{data.class}}{% endif %}'
  {% if data.style %}style='{{data.style}}'{% endif %}>

  {% if data.label %}<div class="label">{{data.label}}</div>{% endif %}
  {% if data.text %}<p>{{data.text}}</p>{% endif %}
  {% if data.inner %}
    {{data.inner}}
  {% endif %}
</div>

""",
"textfield": """\
{% if data.label %}<label for="{{data.id}}">{{data.label}}</label>{% endif %}
<input type="text" 
  {% if data.id %}id='{{data.id}}'{% endif %}
  class='box {% if data.class %}{{data.class}}{% endif %}'
  {% if data.style %}style='{{data.style}}'{% endif %}
  {% if data.text %}placeholder="{{data.text}}"{% endif %}
  {% if data.cols %}size="{{data.cols}}"{% endif %}/>

""",
"textarea": """\
{% if data.label %}<label for="{{data.id}}">{{data.label}}</label>{% endif %}
<textarea
  {% if data.id %}id='{{data.id}}'{% endif %}
  class='box {% if data.class %}{{data.class}}{% endif %}'
  {% if data.style %}style='{{data.style}}'{% endif %}
  {% if data.text %}placeholder="{{data.text}}"{% endif %}
  {% if data.cols %}cols="{{data.cols}}"{% endif %}
  {% if data.rows %}rows="{{data.rows}}"{% endif %} ></textarea>
    
""",
"select": """\
{% if data.label %}<label for="{{data.id}}">{{data.label}}</label>{% endif %}
<select
  {% if data.id %}id='{{data.id}}'{% endif %}
  class='box {% if data.class %}{{data.class}}{% endif %}'
  {% if data.style %}style='{{data.style}}'{% endif %}>
  {% if data.text %}<option value="">{{data.text}}</option>{% endif %}
</select>

""",
"radio": """\
<input type="radio"
  {% if data.id %}id='{{data.id}}'{% endif %}
  class='box {% if data.class %}{{data.class}}{% endif %}'
  {% if data.style %}style='{{data.style}}'{% endif %}
  {% if data.cols %}size="{{data.cols}}"{% endif %}/>
<label for="{{data.id}}">{{data.label}}</label>

""",
"checkbox": """\
<input type="checkbox"
  {% if data.id %}id='{{data.id}}'{% endif %}
  class='box {% if data.class %}{{data.class}}{% endif %}'
  {% if data.style %}style='{{data.style}}'{% endif %} />
<label for="{{data.id}}">{{data.label}}</label>

""",
"button": """\
<button
  {% if data.id %}id='{{data.id}}'{% endif %}
  class='box {% if data.class %}{{data.class}}{% endif %}'
  {% if data.style %}style='{{data.style}}'{% endif %}>
  {% if data.label %}{{data.label}}{% endif %}
</button>

""",
"flex":"""\
<div 
  {% if data.id %}id='{{data.id}}'{% endif %}
  {% if data.class %}class='flex {{data.class}}'{% endif %}
  {% if data.style %}style='display:flex;{{data.style}}'{% endif %}>

  {% if data.label %}<div class="box-label">{{data.label}}</div>{% endif %}
  {% if data.text %}<p>{{data.text}}</p>{% endif %}
  {% if data.inner %}
    {{data.inner}}
  {% endif %}
</div>

""",
    "grid":"""\
<div 
  {% if data.id %}id='{{data.id}}'{% endif %}
  {% if data.class %}class='{{data.class}}'{% endif %}
  {% if data.style %}style='display:grid;width:100%;height:100%;{{data.style}}'{% endif %}>

  {% if data.label %}<div class="box-label">{{data.label}}</div>{% endif %}
  {% if data.text %}<p>{{data.text}}</p>{% endif %}
  {% if data.inner %}
    {{data.inner}}
  {% endif %}
</div>

""",
    "p": """\
<p
  {% if data.id %}id='{{data.id}}'{% endif %}
  {% if data.class %}class='{{data.class}}'{% endif %}
  {% if data.style %}style='{{data.style}}'{% endif %}>

  {% if data.text %}{{data.text}}{% endif %}</p>

""",
}

def grid_size(p):
    # sizeはfullまたはNxNの形式
    # fullの場合は
    if p == "full":
        return "width:100%; height:100%;"
    elif p.startswith("w"):
        # wの場合は、widthを指定する
        width_value = p[1:]  # "w"を除いた部分を取得
        if width_value.isdigit():
            return f"width:{width_value}px; height:auto;"
        else:
            raise ValueError(f"Invalid width value: {width_value}")
    elif "x" in p:
        # NxNの場合は、widthとheightを指定する
        size = p.split("x")
        if len(size) != 2:
            raise ValueError(f"Invalid size format: {p}")
        if not size[0].isdigit() or not size[1].isdigit():
            raise ValueError(f"Invalid size format: {p}")
        # size[0]がwidth、size[1]がheight
        width = size[0]
        height = size[1]
        return f"width:{width}%; height:{height}%;"
    else:
        # それ以外の形式はエラー
        raise ValueError(f"Invalid size format: {p}")

def grid_tile(p):
    # tileはNxNの形式
    # NxNの場合は、widthとheightを指定する
    if "x" in p:
        size = p.split("x")
        if len(size) != 2:
            raise ValueError(f"Invalid tile format: {p}")
        if not size[0].isdigit() or not size[1].isdigit():
            raise ValueError(f"Invalid tile format: {p}")
        # size[0]がwidth、size[1]がheight
        # それぞれのサイズをfrで指定する
        width = f"{size[0]}"
        height = f"{size[1]}"
        return f"grid-template-columns: repeat({width}, 1fr); grid-template-rows: repeat({height}, 1fr);"
    else:
        # それ以外の形式はエラー
        raise ValueError(f"Invalid tile format: {p}")

def flex_size(p):
    # sizeはfullまたはNxNの形式
    # fullの場合は
    if p == "full":
        return "width:100%; height:100%;"
    elif "x" in p:
        # NxNの場合は、widthとheightを指定する
        size = p.split("x")
        if len(size) != 2:
            raise ValueError(f"Invalid size format: {p}")
        if not size[0].isdigit() or not size[1].isdigit():
            raise ValueError(f"Invalid size format: {p}")
        # size[0]がwidth、size[1]がheight
        # それぞれのサイズをパーセントで指定する
        width = size[0]
        height = size[1]
        return f"width:{width}%; height:{height}%;"
    else:
        # それ以外の形式はエラー
        raise ValueError(f"Invalid size format: {p}")

def flex_direction(p):
    # directionはrowまたはcolumnの形式
    if p == "row":
        return "flex-direction: row;"
    elif p == "column":
        return "flex-direction: column;"
    else:
        # それ以外の形式はエラー
        raise ValueError(f"Invalid direction format: {p}")
def flex_wrap(p):
    # wrapはwrapまたはnowrapの形式
    if p == "wrap":
        return "flex-wrap: wrap;"
    elif p == "nowrap":
        return "flex-wrap: nowrap;"
    else:
        # それ以外の形式はエラー
        raise ValueError(f"Invalid wrap format: {p}")
def flex_align(p):
    # alignはstart、center、endの形式
    if p == "start":
        return "align-items: flex-start;"
    elif p == "center":
        return "align-items: center;"
    elif p == "end":
        return "align-items: flex-end;"
    else:
        # それ以外の形式はエラー
        raise ValueError(f"Invalid align format: {p}")
def flex_justify(p):
    # justifyはstart、center、endの形式
    if p == "start":
        return "justify-content: flex-start;"
    elif p == "center":
        return "justify-content: center;"
    elif p == "end":
        return "justify-content: flex-end;"
    else:
        # それ以外の形式はエラー
        raise ValueError(f"Invalid justify format: {p}")
def flex_item(p):
    # itemはstart、center、endの形式
    if p == "start":
        return "align-self: flex-start;"
    elif p == "center":
        return "align-self: center;"
    elif p == "end":
        return "align-self: flex-end;"
    else:
        # それ以外の形式はエラー
        raise ValueError(f"Invalid item format: {p}")
def flex_order(p):
    # orderは整数の形式
    if p.isdigit():
        return f"order: {p};"
    else:
        # それ以外の形式はエラー
        raise ValueError(f"Invalid order format: {p}")
def flex_grow(p):
    # growは整数の形式
    if p.isdigit():
        return f"flex-grow: {p};"
    else:
        # それ以外の形式はエラー
        raise ValueError(f"Invalid grow format: {p}")
def flex_shrink(p): 
    # shrinkは整数の形式
    if p.isdigit():
        return f"flex-shrink: {p};"
    else:
        # それ以外の形式はエラー
        raise ValueError(f"Invalid shrink format: {p}")
def flex_basis(p):
    # basisは整数の形式
    if p.isdigit():
        return f"flex-basis: {p};"
    else:
        # それ以外の形式はエラー
        raise ValueError(f"Invalid basis format: {p}")
def box_gpos(p):
    # gsizeはNxNの形式
    # NxNの場合は、grid-columnとgrid-rowを指定する
    # それ以外の形式はエラー
    if "/" in p:
        size = p.split("/")
        if len(size) != 2:
            raise ValueError(f"Invalid gsize format: {p}")
        # size[0]がgrid-column、size[1]がgrid-row
        x = size[0].split("-")
        y = size[1].split("-")
        # FIXME: width, heightの値が一つしかない場合は、w-h形式。二つある場合はw1/22の形式に変換
        if len(x) == 1:
            width = f"{x[0]}"
        elif len(x) == 2:
            width = f"{x[0]} / {x[1]}"
        else:
            raise ValueError(f"Invalid gsize format: {p}")
        if len(y) == 1:
            height = f"{y[0]}"
        elif len(y) == 2:
            height = f"{y[0]} / {y[1]}"
        else:
            raise ValueError(f"Invalid gsize format: {p}")
        return f"grid-column: {width}; grid-row: {height};"
    else:
        # それ以外の形式はエラー
        raise ValueError(f"Invalid gsize format: {p}")
def box_gcol(p):
    # gcolはN-Nの形式
    # N-Nの場合は、grid-columnをN\Nの形で指定する
    # Nのみの指定の場合は、位置だけを指定する
    # それ以外の形式はエラー
    if "/" in p:
        size = p.split("/")
        if len(size) != 2:
            raise ValueError(f"Invalid gsize format: {p}")
        return f"grid-column: {p};"
    elif p.isdigit():
        return f"grid-column: {p};"
    else:
        # それ以外の形式はエラー
        raise ValueError(f"Invalid gsize format: {p}")
def box_grow(p):
    # growは整数の形式
    if "/" in p:
        size = p.split("/")
        if len(size) != 2:
            raise ValueError(f"Invalid grow format: {p}")
        # size[0]がwidth、size[1]がheight
        # それぞれのサイズを文字列のまま指定する
        return f"grid-row: {p};"
    elif p.isdigit():
        return f"grit-row: {p};"
    else:
        # それ以外の形式はエラー
        raise ValueError(f"Invalid grow format: {p}")
def box_size(p):
    # sizeはNxNの形式
    # NxNの場合は、widthとheightを指定する
    # それぞれのサイズを文字列のまま指定する
    # それ以外の形式はエラー
    if "x" in p:
        size = p.split("x")
        if len(size) != 2:
            raise ValueError(f"Invalid size format: {p}")
        if not size[0].isdigit() or not size[1].isdigit():
            raise ValueError(f"Invalid size format: {p}")
        # size[0]がwidth、size[1]がheight
        width = size[0]
        height = size[1]
        return f"width:{width}; height:{height};"
    else:
        # それ以外の形式はエラー
        raise ValueError(f"Invalid size format: {p}")

def box_scroll(p):
    if p == "x":
        return "overflow-x: scroll;"
    elif p == "y":
        return "overflow-y: scroll;"
    elif p == "both":
        return "overflow: scroll;"
    else:
        # それ以外の形式はエラー
        raise ValueError(f"Invalid scroll format: {p}")

basic_methods = {
    "grid_size": grid_size,
    "grid_tile": grid_tile,
    "flex_size": flex_size,
    "flex_direction": flex_direction,
    "flex_wrap": flex_wrap,
    "flex_align": flex_align,
    "flex_justify": flex_justify,
    "flex_item": flex_item,
    "flex_order": flex_order,
    "flex_grow": flex_grow,
    "flex_shrink": flex_shrink,
    "flex_basis": flex_basis,
    "box_size": box_size,
    "box_gpos": box_gpos,
    "box_gcol": box_gcol,
    "box_grow": box_grow,
    "box_scroll": box_scroll,
}