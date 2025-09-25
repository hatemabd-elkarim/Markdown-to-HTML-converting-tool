import pytest
from converter import convert_markdown

def test_convert_markdown_complex_nested_lists_with_table():
    md = [
        "# Heading 1",
        "This is a paragraph.",
        "- Item A",
        "    - Subitem A1",
        "        - Subsubitem A1a",
        "    - Subitem A2",
        "- Item B",
        "1. First",
        "    1. a",
        "        1. i",
        "        2. ii",
        "    2. b",
        "2. Second",
        "    1. c",
        "## Heading 2",
        "| Name | Age |",
        "|------|-----|",
        "| Alice | 25 |",
        "| Bob   | 30 |"
    ]

    html = convert_markdown(md)

    expected = [
        "<h1>Heading 1</h1>",
        "<p>This is a paragraph.</p>",
        "<ul>",
        "<li>Item A</li>",
        "<ul>",
        "<li>Subitem A1</li>",
        "<ul>",
        "<li>Subsubitem A1a</li>",
        "</ul>",
        "<li>Subitem A2</li>",
        "</ul>",
        "<li>Item B</li>",
        "</ul>",
        "<ol>",
        "<li>First</li>",
        "<ol>",
        "<li>a</li>",
        "<ol>",
        "<li>i</li>",
        "<li>ii</li>",
        "</ol>",
        "<li>b</li>",
        "</ol>",
        "<li>Second</li>",
        "<ol>",
        "<li>c</li>",
        "</ol>",
        "</ol>",
        "<h2>Heading 2</h2>",
        '<table border="1">',
        "<tr>\n<th>Name</th>\n<th>Age</th>\n</tr>",
        "<tr>\n<td>Alice</td>\n<td>25</td>\n</tr>",
        "<tr>\n<td>Bob</td>\n<td>30</td>\n</tr>",
        "</table>"
    ]

    assert html == expected
