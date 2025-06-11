import json
import csv


def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_output(nodes, edges, output_path, fmt):
    if fmt == "json":
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump({"nodes": nodes, "edges": edges}, f, indent=2)
    else:
        with open(output_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["source", "target", "type"])
            writer.writeheader()
            for edge in edges:
                writer.writerow(edge)
