def build_uuid_map(nodes):
    return {node["uri"]: node["id"] for node in nodes}
