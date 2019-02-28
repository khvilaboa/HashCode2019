
import argparse
from models import *
import re

class Handler:
    def __init__(self, filename):
        self.photos = []

        with open(filename, 'r') as f:
            self.num_photos = f.readline()
            ind = 0

            for line in f.readlines():
                match = re.match("(H|V) ([0-9]+) (.*)", line)
                if match:
                    orientation, num_tags, tags = match.groups()
                    photo = Photo(ind, set(tags.split()), orientation is 'H')
                    self.photos.append(photo)
                    ind += 1

        self.output("test.txt", self.create_slideshow_bruteforce(self.photos))

    def output(self, filename, slideshow):
        with open(filename, 'w') as f:
            f.write(str(len(slideshow.slides)) + "\n")
            for slide in slideshow.slides:
                f.write(slide.to_output_file() + "\n")

    def create_slideshow_bruteforce(self, photos):
        slideshow = SlideShow()
        slide_set = set()
        for photo in photos:
            slide_set.add(Slide(photo))

        current_slide = slide_set.pop()
        slideshow.append(current_slide)
        while len(slide_set) > 0:
            best_match = None
            best_match_points = -1
            for candidate in slide_set:
                points = current_slide.interest_factor(candidate)
                if points > best_match_points:
                    best_match = candidate
                    best_match_points = points
            current_slide = best_match
            slide_set.remove(best_match)

        return slideshow






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
