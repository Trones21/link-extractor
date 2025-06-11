---
id: "0869998d-6f54-488b-bd00-15433b4773a5" 
title: "Link Extractor" 
Last_Update: "" 
Tags: [""]
---

import React from 'react';
import TrafficLightProgress from '@site/src/components/TrafficLightProgress';


The Link Extractor Tool is a Go-based CLI utility designed to parse markdown files and extract all links in a structured format for analysis and integration. It generates outputs in CSV and JSON formats, detailing the relationships between source files and their internal or external links, including optional metadata like line numbers and character positions. This tool serves as a standalone utility for auditing links or as a data preparation step for the [Interconnectedness Visualization Tool](6f28e14b-d01e-4afa-827b-abc0a81f4cad), enabling users to create interactive graphs that showcase the relationships between documents and external resources. With its simplicity and versatility, the Link Extractor Tool bridges the gap between content and visualization.

- [Repo](https://github.com/Trones21/link-extractor)
- Status: <TrafficLightProgress progress={0} finalLightPause={1100} offTimeout={900}/> MVP Done
    - Notes