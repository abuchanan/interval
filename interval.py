from functools import total_ordering

__version__ = '0.1'

@total_ordering
class Interval(object):
    '''0-based, half-open interval'''

    def __init__(self, start, end):
        self.start = start
        self.end = end

    @property
    def _key(self):
        return (self.start, self.end)

    def __eq__(self, other):
        return self._key == other._key

    def __lt__(self, other):
        return self._key < other._key

    def __hash__(self):
        return hash(self._key)

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
