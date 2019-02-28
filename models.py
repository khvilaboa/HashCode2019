
# TODO: Define models.

class Photo:
    def __init__(self, tags: set, horizontal: bool):
        self.tags = tags
        self.horizontal = horizontal

class Slide:
    def __init__(self, photo1, photo2 = None):
        self.photo1 = photo1
        self.photo2 = photo2

        if photo2 is None:
            self.tags = self.photo1.tags.copy()
        else:
            self.tags = photo1.tags | photo2.tags

    def similitude_with(self, other_slide):
        common_tags  = self.tags + other_slide.tags
        tags_1_not_2 = self.tags - other_slide.tags
        tags_2_not_1 = other_slide.tags - self.tags
        return min(len(common_tags), len(tags_1_not_2), len(tags_2_not_1))

class SlideShow:
    def __init__(self):
        self.slides = []

    def score(self):
        points = 0
        for first, second in zip(self.slides[:-1], self.slides[1:])
            points += first.similitude_with(second)



