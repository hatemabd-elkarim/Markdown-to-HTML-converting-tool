import sys, re, argparse

def convert_line(line: str) -> str:
    """
    Parse the line to a heading, list item, a line of paragragh, et cetra
    
    :param line: markdown line
    :type line: str
    :return: html line
    :rtype: str
    """
    # heading
    if matches := re.search(r'^(#+)\s+(.*)', line):
        level = len(matches.group(1))
        text = matches.group(2)
        if level <= 6:
            return f"<h{level}>{text.strip()}</h{level}>"
        else:
            return f"<p>{text.strip()}</p>"
    
    # unordered list item
    elif matches := re.match(r'[ \t]*(\*|-|\+)\s+(.*)', line):  
        text = matches.group(2)
        return f"<li>{text.strip()}</li>"
    
    # ordered list item
    elif re.match(r'[ \t]*\d+\.\s+', line):  
        text = line.split(maxsplit=1)[1]
        return f"<li>{text.strip()}</li>"
    
    # url
    elif matches := re.search(r'^\[(.+?)\]\((\S+)(?:\s+"(.+)")?\)$', line):
        text, url, title = matches.groups()
        if title:
            return f'<a href="{url.strip()}" title="{title.strip()}">{text.strip()}</a>'
        else:
            return f'<a href="{url.strip()}">{text.strip()}</a>'
    
    # image
    elif matches := re.search(r'^!\[(.+?)\]\((\S+)(?:\s+"(.+)")?\)$', line):
        text, url, title = matches.groups()
        if title:
            return f'<img src="{url.strip()}" alt="{text.strip()}" title="{title.strip()}">'
        else:
            return f'<img src="{url.strip()}" alt="{text.strip()}">'
    

    # table row
    elif re.search(r'^(?:\|\s*([^|]+)\s*)+\|?$',line):
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        tds = ""
        for cell in cells:
            tds += f"<td>{cell}</td>\n"
        return f"<tr>\n{tds}</tr>"
        
    # horizontal row
    elif line == "---":
        return f'<hr>'
    
    # paragrapgh
    else:
        return f'<p>{line.strip()}</p>'