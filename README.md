# Markdown to HTML Converter

#### Video Demo:  <[URL HERE](https://youtu.be/7dU5XGLi1Ek)>
#### Description:

This project is a **Markdown to HTML converter** built in Python. It allows users to transform Markdown-formatted text into fully structured HTML pages with proper formatting. The tool supports:

- **Headings**: All levels of Markdown headings (`#`, `##`, `###`, etc.) are converted to corresponding HTML `<h1>`–`<h6>` tags.
- **Paragraphs**: Consecutive lines of text are wrapped in `<p>` tags for proper HTML paragraph formatting and automatic word wrapping.
- **Lists**: Both **unordered (`-`, `*`, `+`)** and **ordered (`1.`, `2.`)** lists are supported, including **nested lists** of any depth.
- **Tables**: Markdown tables are parsed and converted into HTML `<table>` elements, with proper `<th>` and `<td>` cells.
- **Links and Images**: Markdown links `[text](url)` are converted into `<a>` tags, and images `![alt](url)` are rendered as `<img>` elements.
- **Inline formatting**: Supports bold, italic, strikethrough, and inline code using Markdown syntax.

The program can read any Markdown file, parse its contents, and generate an HTML file with all the formatting applied. This makes it ideal for:

- Quickly converting documentation or notes to HTML.
- Building static web pages from Markdown content.
- Learning how Markdown parsing and HTML generation works in Python.

**Key Features**:

- Handles nested structures like lists and tables.
- Supports images with optional titles.
- Generates valid HTML5 output with `<html>`, `<head>`, and `<body>` tags.
- Easily extendable for additional Markdown features.

**Usage**:

```bash
python project.py --file example.md
```

The output will be saved as `output.html` in the same directory.


