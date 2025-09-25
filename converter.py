import sys, re, argparse
from parser import convert_line
from formatter import apply_inline_formatting

html  = []
table = []
ulist = []
olist = []

def convert_markdown(md_text: list[str]) -> list[str]:
    """
    convert markdown lines into html lines with help of parser and formatter

    :param line: markdown text lines
    :type line: list of str
    :return: html text lines
    :rtype: list of str
    """
    global html, table, ulist, olist
    # Reset
    html = []
    table = []
    ulist = []
    olist = []

    for i, line in enumerate(md_text):
        if re.search(r'^(?:\|\s*([^|]+)\s*)+\|?$',line):
            if i+1 < len(md_text) and re.search(r'^(?:\|\s*(-+)\s*)+\|?$',md_text[i+1]): # new table
               table = []
            table.append(line)
        
        elif re.match(r'[ \t]*(\*|-|\+)\s+', line):
            if table:
                handle_table()
            ulist.append(line)

        elif re.match(r'[ \t]*\d+\.\s+', line):
            if table:
                handle_table()
            if ulist:
                handle_ulist()
            olist.append(line)

        else:
            if table:
                handle_table()
            if ulist:
                handle_ulist()
            if olist:
                handle_olist()
            html.append(convert_line(line))
    if table:
        handle_table()
    if ulist:
        handle_ulist()
    if olist:
        handle_olist()
    return html

# helper functions
def handle_table():
    global table
    html.append('<table border="1">')

    # header row
    metadata = [cell.strip() for cell in table[0].strip("|").split("|")]
    ths = ""
    for cell in metadata:
        ths += f"<th>{cell}</th>\n"
    html.append(f"<tr>\n{ths}</tr>")

    # data rows (skip rows[1] because it's the --- separator)
    for row in table[2:]:
        html.append(convert_line(row))
    html.append("</table>")
    table = []

def handle_ulist():
    global ulist
    level = 0
    html.append("<ul>")
    for item in ulist:
        # count indentation (each indentation increases level by 1)
        num_tabs = count_indent(item)

        # go deeper
        while num_tabs > level:
            html.append("<ul>")
            level += 1
        # go shallower
        while num_tabs < level:
            html.append("</ul>")
            level -= 1

        html.append(convert_line(item))

    # Close any remaining <ul>
    while level > 0:
        html.append("</ul>")
        level -= 1

    html.append("</ul>")
    ulist = []


def handle_olist():
    global olist
    level = 0
    html.append("<ol>")
    for item in olist:
        num_tabs = count_indent(item)
        

        while num_tabs > level:
            html.append("<ol>")
            level += 1

            
        while num_tabs < level:
            html.append("</ol>")
            level -= 1

        html.append(convert_line(item))

    # close any remaining levels
    while level > 0:
        html.append("</ol>")
        level -= 1
    html.append("</ol>")
    olist = []


def count_indent(line: str) -> int:
    """
    Count indentation level based on spaces or tabs.
    - Any leading spaces (each 4 count as 1 level)
    - Each tab counts as 1 level
    """
    match = re.match(r'^[ \t]*', line)
    if not match:
        return 0

    indent = match.group(0)
    num_spaces = indent.count(" ")

    return (num_spaces // 4)
