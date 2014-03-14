from functools import total_ordering


__version__ = '1.0.1'


@total_ordering
class ComparisonMixin(object):

    @property
    def _key(self):
        return (self.start, self.end)

    def __eq__(self, other):
        return self._key == other._key

    def __lt__(self, other):
        return self._key < other._key

    def __hash__(self):
        return hash(self._key)
