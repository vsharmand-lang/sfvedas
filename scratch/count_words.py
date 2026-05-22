import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))
import generate_tutorials

bodies = {
    'sec-016': generate_tutorials.sec_016_body,
    'sec-017': generate_tutorials.sec_017_body,
    'sec-018': generate_tutorials.sec_018_body,
    'sec-019': generate_tutorials.sec_019_body,
    'sec-020': generate_tutorials.sec_020_body
}

for slug, body in bodies.items():
    words = len(body.split())
    print(f"{slug} word count: {words}")
