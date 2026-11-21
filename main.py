# main.py: copy the entry image to the output directory (stdlib only).
# The image sums up Saturday 21 November 2026: the AI-led market rout,
# Russia's strikes on Ukraine and Poland, the Trump-Putin-Xi summit
# aftermath, Hormuz tanker attacks, the FBI/USDA hack, a pancreatic
# cancer pill result, and COP31 running past its deadline.
import os
import shutil

here = os.path.dirname(os.path.abspath(__file__))
out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
src = os.path.join(here, "entry.png")
dst = os.path.join(out, "entry.png")
shutil.copyfile(src, dst)
# The gate takes a whole PNG: fail loudly if the copy is not one.
with open(dst, "rb") as f:
    assert f.read(8) == b"\x89PNG\r\n\x1a\n", "entry.png is not a PNG"
print("wrote", dst, os.path.getsize(dst), "bytes")
