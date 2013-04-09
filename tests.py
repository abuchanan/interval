from nose.tools import eq_, ok_, raises

from interval import Interval


def test_Interval():
    a = Interval(10, 20)
    eq_(a.start, 10)
    eq_(a.end, 20)
    eq_(a.length, 10)

    ok_(10 in a)
    ok_(19 in a)
    ok_(9 not in a)
    ok_(20 not in a)

    b = Interval(10, 12)
    ok_(b in a)
    ok_(a not in b)
    ok_(a.overlaps(b))
    ok_(b.overlaps(a))

    c = Interval(5, 10)
    ok_(c not in a)
    ok_(a not in c)
    ok_(not a.overlaps(c))
    ok_(not c.overlaps(a))

    d = Interval(5, 11)
    ok_(d not in a)
    ok_(a not in d)
    ok_(a.overlaps(d))
    ok_(d.overlaps(a))

    e = Interval(20, 25)
    ok_(e not in a)
    ok_(a not in e)
    ok_(not a.overlaps(e))
    ok_(not e.overlaps(a))

    f = Interval(19, 25)
    ok_(f not in a)
    ok_(a not in f)
    ok_(a.overlaps(f))
    ok_(f.overlaps(a))

    ok_(b < a)

    h = Interval(10, 20)
    ok_(a == h)

    eq_(hash(a), hash(h))
    i = set([a, h])
    eq_(len(i), 1)
