import sys, re, argparse
from parser import convert_line

def test_heading():
    assert convert_line("# Heading") == "<h1>Heading</h1>"
    assert convert_line("### Subheading") == "<h3>Subheading</h3>"
    assert convert_line("####### Too big") == "<p>Too big</p>"

def test_unordered_list():
    assert convert_line("- Item") == "<li>Item</li>"
    assert convert_line("* Another") == "<li>Another</li>"
    assert convert_line("   + Plus") == "<li>Plus</li>"

def test_ordered_list():
    assert convert_line("1. First") == "<li>First</li>"
    assert convert_line("   42. Meaning") == "<li>Meaning</li>"

def test_image():
    assert convert_line('![Alt](img.png)') == '<img src="img.png" alt="Alt">'
    assert convert_line('![Alt](img.png "Caption")') == '<img src="img.png" alt="Alt" title="Caption">'

def test_table_row():
    line = "| Name | Age |"
    expected = "<tr>\n<td>Name</td>\n<td>Age</td>\n</tr>"
    assert convert_line(line) == expected

def test_horizontal_rule():
    assert convert_line("---") == "<hr>"

def test_paragraph():
    assert convert_line("Just text") == "<p>Just text</p>"
