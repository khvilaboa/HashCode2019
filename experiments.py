
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

def group_quantities(pairs):
    c = defaultdict(int)

    for pair in pairs:
        c[pair[0]] += 1

    return sorted(c.items(), reverse=True)


filenames = ["a_example.txt", "b_lovely_landscapes.txt", "c_memorable_moments.txt", "d_pet_pictures.txt", "e_shiny_selfies.txt"]

if __name__ == "__main__":

    for filename in filenames:
        print("\n" + filename + "\n")
        filename = "data/" + filename

        handler = Handler(filename)

        tag_count = count_tags(handler)
        print(count_tags(handler)[:100])

        groups = group_quantities(tag_count)
        print(groups[:100])
