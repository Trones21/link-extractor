package main

import (
	"flag"
	"fmt"
	"log"

	"github.com/Trones21/link-extractor-tool/internal/extractor"
)

func main() {
	path := flag.String("file", "", "Markdown file to parse")
	flag.Parse()

	if *path == "" {
		log.Fatal("Please provide a file path using --file")
	}

	content, err := extractor.ReadFile(*path)
	if err != nil {
		log.Fatalf("Error reading file: %v", err)
	}

	links := extractor.ExtractLinks(content)
	for _, link := range links {
		fmt.Printf("Text: %-20s → URL: %s\n", link.Text, link.URL)
	}
}
