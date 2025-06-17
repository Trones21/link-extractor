import os


def get_markdown_files(directory):
    markdown_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md") or file.endswith(".mdx"):
                print("Found markdown file: ", os.path.join(root, file))
                markdown_files.append(os.path.join(root, file))
    return markdown_files
