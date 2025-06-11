import re


def extract_frontmatter(path, content):
    # Stub: just use filename as label
    return {"id": path, "label": path.split("/")[-1], "type": "markdown"}


def extract_links(source_path, content):
    link_pattern = re.compile(r"\[(.*?)\]\((.*?)\)")
    edges = []
    for match in link_pattern.finditer(content):
        target = match.group(2)
        link_type = "external" if target.startswith("http") else "internal"
        edges.append({"source": source_path, "target": target, "type": link_type})
    return edges
