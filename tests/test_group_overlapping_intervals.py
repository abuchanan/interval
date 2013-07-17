import nose
from nose.tools import eq_

from interval.closed import Interval, group_overlapping_intervals



def test_empty_intervals_arg():
    x = []
    z = group_overlapping_intervals(x)
    eq_(z, None)


def test_single_Interval():
    x = [Interval(10, 20)]
    groups = group_overlapping_intervals(x)

    eq_(len(groups), 1)
    z = groups[0]
    eq_(z.start, 10)
    eq_(z.end, 20)
    eq_(z.intervals, x)


def test_simple_non_overlapping():
    x = [Interval(10, 20), Interval(25, 35)]
    groups = group_overlapping_intervals(x)

    eq_(len(groups), 2)
    y = groups[0]
    eq_(y.start, 10)
    eq_(y.end, 20)
    eq_(y.intervals, [x[0]])

    z = groups[1]
    eq_(z.start, 25)
    eq_(z.end, 35)
    eq_(z.intervals, [x[1]])


def test_simple_overlapping():
    x = [Interval(10, 20), Interval(19, 35)]
    groups = group_overlapping_intervals(x)

    eq_(len(groups), 1)
    y = groups[0]
    eq_(y.start, 10)
    eq_(y.end, 35)
    eq_(y.intervals, x)

def test_simple_end_to_end():
    x = [Interval(10, 20), Interval(21, 35)]
    groups = group_overlapping_intervals(x)

    eq_(len(groups), 2)
    y = groups[0]
    eq_(y.start, 10)
    eq_(y.end, 20)
    eq_(y.intervals, [x[0]])

    z = groups[1]
    eq_(z.start, 21)
    eq_(z.end, 35)
    eq_(z.intervals, [x[1]])

def test_simple_end_to_end_given_leeway():
    x = [Interval(10, 20), Interval(21, 35)]
    groups = group_overlapping_intervals(x, leeway=1)

    eq_(len(groups), 1)
    y = groups[0]
    eq_(y.start, 10)
    eq_(y.end, 35)
    eq_(y.intervals, x)

def test_simple_overlapping_given_leeway():
    x = [Interval(10, 20), Interval(25, 35)]
    groups = group_overlapping_intervals(x, leeway=5)

    eq_(len(groups), 1)
    y = groups[0]
    eq_(y.start, 10)
    eq_(y.end, 35)
    eq_(y.intervals, x)


def test_simple_non_overlapping_given_leeway():
    x = [Interval(10, 20), Interval(26, 35)]
    groups = group_overlapping_intervals(x, leeway=5)

    eq_(len(groups), 2)
    y = groups[0]
    eq_(y.start, 10)
    eq_(y.end, 20)
    eq_(y.intervals, [x[0]])

    z = groups[1]
    eq_(z.start, 26)
    eq_(z.end, 35)
    eq_(z.intervals, [x[1]])

def test_contained_overlap():
    x = [Interval(10, 40), Interval(26, 35)]
    groups = group_overlapping_intervals(x)

    eq_(len(groups), 1)
    y = groups[0]
    eq_(y.start, 10)
    eq_(y.end, 40)
    eq_(y.intervals, x)


    # Same test, but give the intervals out of order
    x = [Interval(26, 35), Interval(10, 40)]
    groups = group_overlapping_intervals(x)

    eq_(len(groups), 1)
    y = groups[0]
    eq_(y.start, 10)
    eq_(y.end, 40)
    eq_(y.intervals, [x[1], x[0]])

def test_allowed_gaps():
    x = [Interval(10, 20), Interval(30, 35)]
    gaps = [Interval(20, 30)]
    groups = group_overlapping_intervals(x, gaps=gaps)

    eq_(len(groups), 1)
    y = groups[0]
    eq_(y.start, 10)
    eq_(y.end, 35)
    eq_(y.intervals, x)


if __name__ == '__main__':
    nose.run()
