import re


def apply_inline_formatting(text: str) -> str:
    """
    Convert inline markdown syntax inside a text string to HTML.
    Handles bold, italic, strikethrough, et cetra

    :param line: unformatted html line 
    :type line: str
    :return: formated html line
    :rtype: str
    """
    # temporarily replace escaped characters
    text = re.sub(r'(\\\*{1,3})', lambda m: 'ESCAPEDAST123' * (len(m.group(1)) - 1), text)
    text = re.sub(r'(\\_{1,3})', lambda m: 'ESCAPEDUND123' * (len(m.group(1)) - 1), text)


    # bold and italic
    text = re.sub(r'(\*\*\*|___)(.*?)\1', lambda m: f"<strong><em>{m.group(2).strip()}</em></strong>", text)

    # bold
    text = re.sub(r'(\*\*|__)(.*?)\1',lambda m: f'<strong>{m.group(2).strip()}</strong>', text)

    # italic
    text = re.sub(r'(\*|_)(.*?)\1', lambda m: f"<em>{m.group(2).strip()}</em>", text)

    # strikthrough
    text = re.sub(r'~~(.*?)~~', lambda m: f"<del>{m.group(1).strip()}</del>", text)

    # links
    text = re.sub(
        r'\[(.+?)\]\((\S+)(?:\s+"(.+)")?\)',
        lambda m: f'<a href="{m.group(2).strip()}"' +
                  (f' title="{m.group(3).strip()}"' if m.group(3) else '') +
                  f'>{m.group(1).strip()}</a>',
        text)

    # restore escaped characters
    text = text.replace('ESCAPEDAST123', '*')
    text = text.replace('ESCAPEDUND123', '_')


    return text    


