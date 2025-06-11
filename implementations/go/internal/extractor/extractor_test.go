package extractor

import "testing"

func TestExtractLinks(t *testing.T) {
	input := `Check [Google](https://google.com) and [Local](/home).`
	expected := 2

	links := ExtractLinks(input)
	if len(links) != expected {
		t.Errorf("Expected %d links, got %d", expected, len(links))
	}

	if links[0].Text != "Google" || links[0].URL != "https://google.com" {
		t.Errorf("First link mismatch: %+v", links[0])
	}
}
