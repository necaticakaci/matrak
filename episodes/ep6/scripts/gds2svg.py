# GDSII to SVG Converter

import gdstk
import sys
import os

if len(sys.argv) < 2:
    print("Usage: python gds2svg.py <file_path>")
    sys.exit(1)

file_path = sys.argv[1]
file_name = os.path.basename(file_path)
file_name_split = os.path.splitext(file_name)[0]
file_name_out = f"{file_name_split}.svg"

gds = gdstk.read_gds(file_path)
cells = gds.top_level()
cells[0].write_svg(file_name_out)
