# cli.py
import argparse
from extractor.main import extract_all


def parse_args():
    parser = argparse.ArgumentParser(description="Markdown Link Extractor")
    parser.add_argument(
        "--dir", required=True, help="Directory to search for markdown files"
    )
    parser.add_argument("--output", required=True, help="Output file path")
    parser.add_argument(
        "--format", choices=["csv", "json"], default="csv", help="Output format"
    )
    return parser.parse_args()


def main():
    args = parse_args()
    extract_all(args.dir, args.output, args.format)


if __name__ == "__main__":
    main()
