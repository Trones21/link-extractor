# extractor/main.py
import re
from .uuid_hashmapper import build_uuid_map
from .filewalker import get_markdown_files
from .io import read_file, write_output
from .parser import extract_links, extract_frontmatter


def attempt_get_target_id(uri):
    uuid_pattern = re.compile(
        r"/([0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12})",
        re.IGNORECASE,
    )

    match = uuid_pattern.search(uri)
    if match:
        uuid = match.group(1)
        return uuid

    return f"ERROR: UUID not found in passed target_uri: {uri}"


def extract_all(input_dir, output_path, fmt):
    filepaths = get_markdown_files(input_dir)
    nodes = []
    edges = []

    for path in filepaths:
        content = read_file(path)
        nodes.append(extract_frontmatter(path, content))

    print(nodes[0])
    uuid_hashmap = build_uuid_map(nodes)
    for path in filepaths:
        content = read_file(path)
        linksRaw = extract_links(path, content)
        for link in linksRaw:
            link["source"] = uuid_hashmap.get(link["source_uri"])
            link["target"] = (
                attempt_get_target_id(link["target_uri"])
                if link["type"] == "internal"
                else link["target_uri"]
            )
            edges.append(link)

    write_output(nodes, edges, output_path, fmt)
