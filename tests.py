from nose.tools import eq_, ok_, raises

from interval import HalfOpen, Closed, ComparisonMixin


def test_HalfOpen():
    a = HalfOpen(10, 20)
    eq_(a.start, 10)
    eq_(a.end, 20)
    eq_(a.length, 10)

    ok_(10 in a)
    ok_(19 in a)
    ok_(9 not in a)
    ok_(20 not in a)

    b = HalfOpen(10, 12)
    ok_(b in a)
    ok_(a not in b)
    ok_(a.overlaps(b))
    ok_(b.overlaps(a))

    c = HalfOpen(5, 10)
    ok_(c not in a)
    ok_(a not in c)
    ok_(not a.overlaps(c))
    ok_(not c.overlaps(a))

    d = HalfOpen(5, 11)
    ok_(d not in a)
    ok_(a not in d)
    ok_(a.overlaps(d))
    ok_(d.overlaps(a))

    e = HalfOpen(20, 25)
    ok_(e not in a)
    ok_(a not in e)
    ok_(not a.overlaps(e))
    ok_(not e.overlaps(a))

    f = HalfOpen(19, 25)
    ok_(f not in a)
    ok_(a not in f)
    ok_(a.overlaps(f))
    ok_(f.overlaps(a))


def test_Closed():
    a = Closed(10, 20)
    eq_(a.start, 10)
    eq_(a.end, 20)
    eq_(a.length, 11)

    ok_(10 in a)
    ok_(20 in a)
    ok_(9 not in a)
    ok_(21 not in a)

    b = Closed(10, 12)
    ok_(b in a)
    ok_(a not in b)
    ok_(a.overlaps(b))
    ok_(b.overlaps(a))

    c = Closed(5, 9)
    ok_(c not in a)
    ok_(a not in c)
    ok_(not a.overlaps(c))
    ok_(not c.overlaps(a))

    d = Closed(5, 10)
    ok_(d not in a)
    ok_(a not in d)
    ok_(a.overlaps(d))
    ok_(d.overlaps(a))

    e = Closed(21, 25)
    ok_(e not in a)
    ok_(a not in e)
    ok_(not a.overlaps(e))
    ok_(not e.overlaps(a))

    f = Closed(20, 25)
    ok_(f not in a)
    ok_(a not in f)
    ok_(a.overlaps(f))
    ok_(f.overlaps(a))


def test_ComparisonMixin():

    class Interval(ComparisonMixin):
        def __init__(self, start, end):
            self.start = start
            self.end = end

    a = Interval(10, 20)
    b = Interval(5, 10)

    ok_(b < a)

    h = Interval(10, 20)
    ok_(a == h)

    eq_(hash(a), hash(h))
    i = set([a, h])
    eq_(len(i), 1)
