
import argparse, sys
from main import Handler
from collections import defaultdict


def count_tags(handler):
    tags = defaultdict(int)

    for photos in handler.photos:
        for tag in photos.tags:
            tags[tag] += 1

    values = sorted([(value, key) for (key, value) in tags.items()], reverse=True)

    return values

if __name__ == "__main__":
    handler = Handler(sys.argv[1])

    print(count_tags(handler)[:100])
