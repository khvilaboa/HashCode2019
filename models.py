
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
        for ind in range(len(self.slides) - 1):
            first = self.slides[ind]
            second = self.slides[ind + 1]

            points += first.similitude_with(second)

        return points


