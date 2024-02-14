#!/bin/bash

if [ "$#" -lt 1 ]; then
    echo "Usage: ./gds2png.sh <file_path>"
    exit 1
fi

file_path=$1
file_name=$(basename "$file_path")
file_name_split="${file_name%.*}"
file_name_out="${file_name_split}.svg"

python3 gds2svg.py "$file_path"

if ! command -v cairosvg &> /dev/null; then
    echo "Error: cairosvg not found."
    exit 1
fi

if [ $? -eq 0 ]; then
    cairosvg "$file_name_out" -o "${file_name_split}.png"
    if [ $? -eq 0 ]; then
        echo "Process successful. PNG file created: ${file_name_split}.png"
    else
        echo "Process failed."
        exit 1
    fi
else
    echo "Error: PNG conversion failed."
    exit 1
fi
