import intervaltree


class Interval(object):
    '''half-open interval'''

    def __init__(self, start, end):
        self.start = start
        self.end = end

    @property
    def length(self):
        return self.end - self.start

    def __contains__(self, other):
        if isinstance(other, int):
            return other >= self.start and other < self.end

        # TODO not sure if I should do error checking here.
        return other.start >= self.start and other.end <= self.end

    def overlaps(self, other):
        return other.start < self.end and other.end > self.start


Tree = intervaltree.IntervalTree
