package extractor

import (
	"os"
	"regexp"
)

type Link struct {
	Text string
	URL  string
}

var mdLinkRegex = regexp.MustCompile(`\[(.*?)\]\((.*?)\)`)

func ReadFile(path string) (string, error) {
	content, err := os.ReadFile(path)
	if err != nil {
		return "", err
	}
	return string(content), nil
}

func ExtractLinks(content string) []Link {
	matches := mdLinkRegex.FindAllStringSubmatch(content, -1)
	var links []Link
	for _, m := range matches {
		if len(m) == 3 {
			links = append(links, Link{Text: m[1], URL: m[2]})
		}
	}
	return links
}
