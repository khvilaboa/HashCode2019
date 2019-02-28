
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
        common_score = len(common_tags)
        first_score  = len(self.tags) - common_score
        second_score = len(other_slide.tags) - common_score
        return min(common_score, first_score, second_score)

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

        for ind in range(len(self.slides) - 1):
            first = self.slides[ind]
            second = self.slides[ind + 1]

            points += first.interest_factor(second)

        return points