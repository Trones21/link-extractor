# Link Extractor Tool

The **Link Extractor Tool** is a lightweight CLI utility for parsing markdown files and extracting all the links contained within them. It’s designed to serve as a foundation for more complex tools, such as visualizing the interconnectedness of documents and external resources.

## Features

- **Extract Markdown Links**: Parse markdown files to extract all links in `[text](url)` format.
- **CSV Output**: Generate a CSV file containing the source, target, and optional metadata like line numbers and character positions.
- **JSON Output**: Export the link data in a structured JSON format suitable for integration with visualization tools or custom applications.
- **Graph Data Support**: Prepare data that can be imported into node visualization tools like the **Interconnectedness Visualization Tool** (coming soon!).

## Use Cases

- **Data Visualization**: Import extracted data into the [Interconnectedness Visualization Tool](#interconnectedness-visualization-tool) to create interactive visualizations of relationships between documents and links.
- **Link Auditing**: Quickly audit links in a markdown directory for broken links or external reference consistency.
- **Data Integration**: Use the extracted data as a starting point for custom workflows or applications.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/link-extractor-tool.git
   ```
2. Navigate to the directory:
   ```bash
   cd link-extractor-tool
   ```
3. Build the binary:
   ```bash
   go build -o link-extractor
   ```
4. (Optional) Install globally:
   ```bash
   mv link-extractor /usr/local/bin/
   ```

## Usage

### Basic Command

```bash
link-extractor.py --dir ./markdown_files --output links.csv
```

### Available Options

| Flag       | Description                                   | Example                                       |
| ---------- | --------------------------------------------- | --------------------------------------------- |
| `--dir`    | Directory containing markdown files to parse. | `--dir ./docs`                                |
| `--output` | Output file path for extracted links.         | `--output links.json` or `--output links.csv` |
| `--format` | Output format: `csv` (default) or `json`.     | `--format json`                               |

### Example Workflow

1. Extract links from a directory of markdown files:
   ```bash
   link-extractor.py --dir ./docs --output links.csv
   ```
2. Import the CSV or JSON output into the [Interconnectedness Visualization Tool](#interconnectedness-visualization-tool) to create a graph of relationships between documents and links.

## Output Formats

### CSV Format

The CSV output contains the following fields:
| Field | Description |
|------------|-----------------------------------------------|
| `source` | The markdown file containing the link. |
| `target` | The URL or file being linked to. |
| `line` | (Optional) The line number where the link appears. |
| `position` | (Optional) The character position in the line. |

### JSON Format

The JSON output is structured as follows:

```json
{
  "nodes": [
    { "id": "file1.md", "type": "markdown", "label": "File 1" },
    { "id": "https://example.com", "type": "external", "label": "Example" }
  ],
  "edges": [
    {
      "source": "file1.md",
      "target": "https://example.com",
      "type": "external"
    }
  ]
}
```

## Integration with Interconnectedness Visualization Tool

The **Link Extractor Tool** is a key component for feeding data into the upcoming [Interconnectedness Visualization Tool](https://github.com/your-username/interconnectedness-visualizer). This visualization tool will enable users to explore the relationships between markdown files and external links in a dynamic, interactive graph format.

---

## Development

### Prerequisites

- Go 1.19 or higher
- Basic understanding of markdown and link formats

### Running Locally

1. Clone the repository and navigate to the project directory.
2. Use the `go run` command for development:
   ```bash
   go run main.go --dir ./markdown_files --output links.json
   ```

### Contributions

Contributions are welcome! Feel free to open issues or submit pull requests to improve the tool.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions, suggestions, or feedback, please contact [link-extractor@gmailisprofessional.com](mailto:link-extractor@gmailisprofessional.com)
