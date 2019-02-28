
import argparse
from models import *
import re

class Handler:
    def __init__(self, filename):
        self.photos = []

        with open(filename, 'r') as f:
            self.num_photos = f.readline()
            ind = 0
            print(self.num_photos)

            for line in f.readlines():
                match = re.match("(H|V) ([0-9]+) (.*)", line)
                if match:
                    orientation, num_tags, tags = match.groups()
                    photo = Photo(ind, orientation is 'H', tags.split())
                    self.photos.append(photo)
                    ind += 1

    def output(self, filename):
        with open(filename, 'w') as f:
            pass  # TODO: Generate ouptut


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='HashCode 2019 submission for the online qualification round')

    parser.add_argument('input_filename', action='store', help='Input file path.')
    parser.add_argument('-o', '--output_filename', action='store', help='Output file pah')
    # parser.add_argument('-e', '--example', action='store', default = 0, type = int, help='Example 1')
    # parser.add_argument('-b', '--bool_value', action='store_true', help='Example 1')
    args = parser.parse_args()

    handler = Handler(args.input_filename)
    # ...
    #handler.output(args.output_filename)
