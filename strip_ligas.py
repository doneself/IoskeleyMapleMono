import fontforge
import glob
import os
import sys

def strip_ligatures(in_font, out_font):
    font = fontforge.open(in_font)
    for lookup in font.gsub_lookups:
        font.removeLookup(lookup)
    font.generate(out_font)
    font.close()

if __name__ == "__main__":
    src_dir = sys.argv[1]
    dst_dir = sys.argv[2]
    os.makedirs(dst_dir, exist_ok=True)
    for f in glob.glob(os.path.join(src_dir, "*.ttf")):
        basename = os.path.basename(f)
        strip_ligatures(f, os.path.join(dst_dir, basename))
