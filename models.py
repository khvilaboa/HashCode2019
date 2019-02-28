
class Photo:
    def __init__(self, id: int, tags: set, horizontal: bool):
        self.id = id
        self.tags = tags
        self.horizontal = horizontal

    def __str__(self):
        return "%d(%s,%s)" % (self.id, "H" if self.horizontal else "V", str(self.tags))

    def __repr__(self):
        return str(self)


class Slide:
    def __init__(self, photo1, photo2 = None):
        self.photo1 = photo1
        self.photo2 = photo2

        if photo2 is None:
            self.tags = self.photo1.tags.copy()
        else:
            self.tags = photo1.tags | photo2.tags

    def interest_factor(self, other_slide):
        common_tags  = self.tags & other_slide.tags
        tags_1_not_2 = self.tags - other_slide.tags
        tags_2_not_1 = other_slide.tags - self.tags
        return min(len(common_tags), len(tags_1_not_2), len(tags_2_not_1))

    def to_output_file(self):
        if self.photo2 is None:
            return str(self.photo1.id)
        else:
            return str(self.photo1.id) + " " + str(self.photo2.id)


class SlideShow:
    def __init__(self):
        self.slides = []

    def append(self, slide):
        self.slides.append(slide)

    def score(self):
        points = 0
        for first, second in zip(self.slides[:-1], self.slides[1:]):
            points += first.interest_factor(second)

        return points