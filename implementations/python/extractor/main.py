# extractor/main.py
from .filewalker import get_markdown_files
from .io import read_file, write_output
from .parser import extract_links, extract_frontmatter


def extract_all(input_dir, output_path, fmt):
    filepaths = get_markdown_files(input_dir)
    nodes = []
    edges = []

    for path in filepaths:
        content = read_file(path)
        nodes.append(extract_frontmatter(path, content))
        edges.extend(extract_links(path, content))

    write_output(nodes, edges, output_path, fmt)
