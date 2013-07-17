import intervaltree


class Interval(object):
    '''closed interval'''

    def __init__(self, start, end):
        self.start = start
        self.end = end

    @property
    def length(self):
        return self.end - self.start + 1

    def __contains__(self, other):
        if isinstance(other, int):
            return other >= self.start and other <= self.end

        # TODO not sure if I should do error checking here.
        return other.start >= self.start and other.end <= self.end

    def overlaps(self, other):
        return other.start <= self.end and other.end >= self.start


class Tree(intervaltree.IntervalTree):

    def insert(self, start, end, value=None):
        return super(Tree, self).insert(start, end + 1, value)

    def find(self, start, end):
        return super(Tree, self).find(start, end + 1)


# TODO reconcile this with halfopen
class MergedInterval(object):

    def __init__(self):
        self.intervals = []
        self.start = None
        self.end = None

    def add(self, interval):
        self.intervals.append(interval)

        if not self.start or self.start > interval.start:
            self.start = interval.start

        if not self.end or self.end < interval.end:
            self.end = interval.end


# TODO reconcile this with halfopen
def group_overlapping_intervals(intervals, gaps=None, leeway=0):

    if not intervals:
        # TODO error here?
        return

    sort_key = lambda interval: interval.start
    intervals = sorted(intervals, key=sort_key)

    if not gaps:
        gaps = []

    gap_index = Tree()
    for gap in gaps:
        gap_index.insert(gap.start, gap.end, gap)

    groups = []

    current = MergedInterval()
    current.add(intervals[0])
    groups.append(current)

    for interval in intervals[1:]:

        mergeable = interval.start <= current.end + leeway

        if not mergeable:

            # Look for allowed gaps that are overlapping or near the end
            # of the last interval.
            useful_gaps = gap_index.find(current.end - 1, current.end + leeway)

            while not mergeable and useful_gaps:
                gap = useful_gaps.pop()
                # After accounting for an allowed gap, are the two intervals mergeable?
                mergeable = interval.start <= gap.end + leeway

        if mergeable:
            current.add(interval)
        else:
            current = MergedInterval()
            current.add(interval)
            groups.append(current)

    return groups
