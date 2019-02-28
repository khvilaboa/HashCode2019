
import argparse
from models import *


class Handler:
    def __init__(self, filename):
        # TODO: Initialize structures.
        with open(filename, 'r') as f:
            params = f.readline()

            for line in f.readlines():
                pass  # TODO: Instanciate models.

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
    handler.output(args.output_filename)
