
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
