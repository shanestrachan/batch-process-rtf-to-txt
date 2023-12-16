# Batch Process RTF to TXT with Normalization

## Overview

This small Python script efficiently converts RTF files to plain text, and also handles plain text input, and applies multiple normalization techniques. It's designed to prepare documents for NLP tokenization by ensuring consistent formatting.

## Requirements

- Python 3.x
- striprtf library (install using `pip install striprtf`)

## Usage

1. Place your RTF or TXT files in the same directory as the script.
2. Run the script. It will process all RTF and TXT files in the directory and create two TXT output files for each input file:
   - `*-single-space.txt`: with reduced whitespace.
   - `*-new-lines.txt`: with sentences separated by new lines.
