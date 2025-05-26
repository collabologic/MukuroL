# MukuroL
MukuroL is a lightweight markup language, designed exclusively for wireframe creation using simple code. Its name carries a subtle play on "ML" (Markup Language), reflecting its minimalistic yet functional approach to structuring UI layouts.

## Overview
MukuroL is a lightweight markup language designed to create wireframes using simple code. Its name reflects a playful nod to "ML" (Markup Language), embodying a minimalist yet functional approach to structuring UI layouts.

## Commands
MukuroL supports the following commands:

### `mkl init`
Initializes a new MukuroL project. Creates `src` and `dist` directories and an empty `mkl.config.yml` file.

**Example:**
```bash
python mkl.py init /path/to/project
```

### `mkl generate`
Generates HTML from `.mkl` files. You can specify a particular file or process all files in the `src` directory.

**Example:**
- To process a single file:
```bash
python mkl.py generate -i src/sample.mkl -o dist/sample.html
```
- To process all files in the `src` directory:
```bash
python mkl.py generate
```

### `mkl watch`
Monitors `.mkl` files in the `src` directory and automatically regenerates HTML when changes are detected.

**Example:**
```bash
python mkl.py watch
```

## Example Syntax
MukuroL uses indentation to represent nested structures. The first word on each line indicates the block type, followed by attributes in the `key:value` format.

```MukuroL
page title:Sample Page
    grid size:full tile:10x10
        box label:Header gpos:1-10/1 text:Header. App logo or title.
        box label:Sidebar gpos:1-3/2-10 text:Sidebar. Contains menus.
            Dashboard
            Search
            Management
            Profile
        box label:Body gpos:3-10/2-10 scroll:y
            grid tile:2x1
                box label:Form gpos:1/1 text:This is where the input form goes
                    textfield id:text label:Text: text:Enter text here cols:50
                    select id:select label:Select text:Choose something
                    textarea id:area label:Textarea: text:You can enter long text here. cols:40 rows:5
                    flex direction:row
                        radio id:radio1 label:Radio Button 1
                        radio id:radio2 label:Radio Button 2
                    flex direction:row
                        checkbox id:checkbox1 label:Checkbox 1
                        checkbox id:checkbox2 label:Checkbox 2
                    button label:Submit!
                box label:Preview gpos:2/1 text:Preview of input results
                    This is where the rendered screen is displayed.
        box label:Footer gpos:1-10/10 text:Footer.
```

## Language Reference

### `page`
Represents a single screen and must be the root element.

- **`title`**: Specifies the page title.

### `box`
A rectangular box rendered on the screen. Except for form components, wireframes are described by placing boxes.

- **`id`**: Assigns a unique ID to the box's HTML element.
- **`class`**: Specifies the CSS class applied to the box.
- **`style`**: Specifies inline styles applied to the box.
- **`label`**: Label text displayed inside the box.
- **`text`**: Text displayed inside the box.
- **`size:{NxN}`**: Specifies the width and height of the box in `NxN` format.
- **`gpos:{N-N}`**: Specifies the position of the box within a grid in `N-N` format.
- **`scroll:[x|y|both]`**: Specifies scroll behavior (`x` for horizontal, `y` for vertical, `both` for both directions).

### `textfield`
A text field form component.

- **`id`**: Assigns a unique ID to the text field's HTML element.
- **`class`**: Specifies the CSS class applied to the text field.
- **`style`**: Specifies inline styles applied to the text field.
- **`label`**: Label text associated with the text field.
- **`text`**: Placeholder text displayed in the text field.
- **`cols`**: Specifies the width of the text field.

### `textarea`
A textarea form component.

- **`id`**: Assigns a unique ID to the textarea's HTML element.
- **`class`**: Specifies the CSS class applied to the textarea.
- **`style`**: Specifies inline styles applied to the textarea.
- **`label`**: Label text associated with the textarea.
- **`text`**: Placeholder text displayed in the textarea.
- **`cols`**: Specifies the number of columns in the textarea.
- **`rows`**: Specifies the number of rows in the textarea.

### `select`
A select box form component.

- **`id`**: Assigns a unique ID to the select box's HTML element.
- **`class`**: Specifies the CSS class applied to the select box.
- **`style`**: Specifies inline styles applied to the select box.
- **`label`**: Label text associated with the select box.
- **`text`**: Initial option text displayed in the select box.

### `radio`
A radio button form component.

- **`id`**: Assigns a unique ID to the radio button's HTML element.
- **`class`**: Specifies the CSS class applied to the radio button.
- **`style`**: Specifies inline styles applied to the radio button.
- **`label`**: Label text associated with the radio button.

### `checkbox`
A checkbox form component.

- **`id`**: Assigns a unique ID to the checkbox's HTML element.
- **`class`**: Specifies the CSS class applied to the checkbox.
- **`style`**: Specifies inline styles applied to the checkbox.
- **`label`**: Label text associated with the checkbox.

### `button`
A button form component.

- **`id`**: Assigns a unique ID to the button's HTML element.
- **`class`**: Specifies the CSS class applied to the button.
- **`style`**: Specifies inline styles applied to the button.
- **`label`**: Label text displayed on the button.

### `grid`
A block for grid layouts. The internal area of this block is divided into specified-sized cells, and child boxes use the `gpos` helper to specify their display position and size.

- **`id`**: Assigns a unique ID to the grid's HTML element.
- **`class`**: Specifies the CSS class applied to the grid.
- **`style`**: Specifies inline styles applied to the grid.
- **`label`**: Label text displayed inside the grid.
- **`text`**: Text displayed inside the grid.
- **`size:[full | NxN]`**: Specifies the overall size of the grid (`full` for full width and height, or `NxN` format).
- **`tile:{NxN}`**: Specifies the arrangement of tiles within the grid in `NxN` format.

### `flex`
Represents a flexbox block. Child boxes are laid out according to the flex attributes specified.

- **`id`**: Assigns a unique ID to the flexbox's HTML element.
- **`class`**: Specifies the CSS class applied to the flexbox.
- **`style`**: Specifies inline styles applied to the flexbox.
- **`label`**: Label text displayed inside the flexbox.
- **`text`**: Text displayed inside the flexbox.
- **`size:[full | NxN]`**: Specifies the width and height of the flexbox (`full` or `NxN` format).
- **`direction:[row | column]`**: Specifies the direction of the flexbox (`row` for horizontal, `column` for vertical).
- **`wrap:[wrap|nowrap]`**: Specifies whether the flexbox wraps (`wrap` or `nowrap`).
- **`align:[start | center | end]`**: Specifies vertical alignment of items within the flexbox (`start`, `center`, `end`).
- **`justify:[start | center | end]`**: Specifies horizontal alignment of items within the flexbox (`start`, `center`, `end`).


[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/collabologic/MukuroL)