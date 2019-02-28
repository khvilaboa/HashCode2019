
import argparse, pickle, os
from models import *
import re
import networkx as nx

class Handler:
    def __init__(self, filename):
        self.photos = []
        self.hphotos = []
        self.vphotos = []
        self.slides = []
        self.graph = None
        self.slideshow = None
        self.filename = filename

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

                    if orientation is 'H':
                        self.hphotos.append(photo)
                    else:
                        self.vphotos.append(photo)

    def output(self, filename):
        if self.slideshow:
            with open(filename, 'w') as f:
                f.write(str(len(self.slideshow.slides)) + "\n")
                for slide in self.slideshow.slides:
                    f.write(slide.to_output_file() + "\n")

    def b_create_slideshow_bruteforce(self):
        slide_set = set()
        for photo in self.photos:
            slide_set.add(Slide(photo))
        return self.create_slideshow_bruteforce(slide_set)

    def generic_create_slideshow_bruteforce(self):
        return self.create_slideshow_bruteforce({Slide(photo) for photo in self.hphotos})

    def create_slideshow_bruteforce(self, slide_set):
        slideshow = SlideShow()
        current_slide = slide_set.pop()
        slideshow.append(current_slide)
        i = 0
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
            slideshow.append(best_match)
            i += 1
            if i % 100 == 0:
                print(i)

        self.slideshow = slideshow

    def photos_to_slides(self):
        for photo in self.hphotos:
            self.slides.append(Slide(photo))

        self.merge_vertical_slides();

    def merge_vertical_slides(self):
        for i in range(self.vphotos):
            if i % 2 == 0:
                self.slides.append(Slide(self.vphotos[i], self.vphotos[i+1]))

    def create_slideshow_from_graph(self):
        self.slideshow  = SlideShow()
        visited = {}
        for node in self.graph:
            visited[node] = False
            
        for node in self.graph:
            if visited[node]:
                continue

            current_node = node
            self.slideshow.append(current_node)
            visited[current_node] = True

            while True:
                best_score = -1;
                candidate = None
                for neighbor in self.graph[current_node]:
                    if visited[neighbor]:
                        continue

                    score = self.graph.edges[current_node, neighbor]['weight']
                    if score > best_score:
                        best_score = score
                        candidate = neighbor

                if candidate is not None:
                    current_node = candidate
                    self.slideshow.append(candidate)
                    visited[candidate] = True
                else:
                    break

    def create_graph(self):
        self.graph = nx.Graph()
        slides = self.slides.copy()

        # Add nodes
        self.graph.add_nodes_from(slides)

        # Add edges
        while len(slides) != 0:
            slide = slides.pop()

            for cmp_slide in slides:
                int_fac = slide.interest_factor(cmp_slide)
                self.graph.add_edge(slide, cmp_slide, weight=int_fac)

        pickle.dump(self.graph, self.filename + ".graph")

    def load_graph(self):
        if os.path.exists(self.filename + ".graph"):
            self.graph = pickle.load(self.filename + ".graph")
        else:
            self.create_graph()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='HashCode 2019 submission for the online qualification round')

    parser.add_argument('input_filename', action='store', help='Input file path.')
    parser.add_argument('-o', '--output_filename', action='store', help='Output file pah')
    parser.add_argument('-f', '--function', action='store', default=None, help='Function')
    parser.add_argument('-g', '--load_graph', action='store_true', help='Create graph')
    # parser.add_argument('-e', '--example', action='store', default = 0, type = int, help='Example 1')
    # parser.add_argument('-b', '--bool_value', action='store_true', help='Example 1')
    args = parser.parse_args()

    handler = Handler(args.input_filename)

    if args.create_graph:
        handler.create_graph()

    if not args.function:
        handler.b_create_slideshow_bruteforce()
    else:
        print("Executing %s..." % args.function)
        getattr(handler, args.function)()

    handler.output("test.txt")

    # ...
    #handler.output(args.output_filename)
