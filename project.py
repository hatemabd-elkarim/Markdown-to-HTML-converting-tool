import sys, re, argparse
from parser import convert_line
from formatter import apply_inline_formatting
from converter import convert_markdown

def main():
    parser =  argparse.ArgumentParser(description="Convert a markdown file to an html file")
    parser.add_argument("--file", help=".md file")
    args = parser.parse_args()

    md = []
    try:
        with open(args.file) as file:
            for line in file:
                md.append(line)
    except(FileNotFoundError):
        sys.exit("cannot open your file")

    html = convert_markdown(md)
    html = [apply_inline_formatting(line) for line in html]

    
    with open("output.html", "w") as file:
        file.write('<!DOCTYPE html>\n<html>\n<head>\n<meta charset="UTF-8">\n<title>Converted Markdown</title>\n</head>\n<body>\n')
        for line in html:
            file.write(line.rstrip("\n")+"\n")
        file.write('</body>\n</html>')


if __name__ == "__main__":
    main()