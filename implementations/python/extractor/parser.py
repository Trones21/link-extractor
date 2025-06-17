import re


# parser.py

import yaml


def extract_frontmatter(filepath, content):
    # Normalize line endings and split lines
    content = content.replace("\r\n", "\n").replace("\r", "\n")
    lines = content.split("\n")

    if len(lines) < 2 or lines[0].strip() != "---":
        raise ValueError(f"{filepath} does not start with front matter")

    frontmatter_lines = []
    for line in lines[1:]:
        if line.strip() == "---":
            break
        frontmatter_lines.append(line)
    else:
        raise ValueError(f"{filepath} front matter not closed properly")

    frontmatter_text = "\n".join(frontmatter_lines)
    data = yaml.safe_load(frontmatter_text)

    return {"id": data.get("id"), "uri": filepath, "frontmatter": data}


def extract_links(source_path, content):
    print("Extracting links on", source_path)
    link_pattern = re.compile(r"\[(.*?)\]\((.*?)\)")
    edges = []
    for match in link_pattern.finditer(content):
        print("Match groups:", match.groups())
        label = match.group(1)
        target = match.group(2)

        print(f"{source_path} → label: {label} | target: {target}")
        link_type = "external" if target.startswith("http") else "internal"
        edges.append(
            {"source_uri": source_path, "target_uri": target, "type": link_type}
        )
    return edges
