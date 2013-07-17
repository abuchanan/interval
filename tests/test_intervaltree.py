from nose.tools import eq_

from interval import halfopen, closed


def test_halfopen_Tree():
    tree = halfopen.Tree()
    tree.insert(10, 20, 'a')
    x = tree.find(10, 10)
    eq_(x, [])


def test_closed_Tree():
    tree = closed.Tree()
    tree.insert(10, 20, 'a')
    x = tree.find(10, 10)
    eq_(x, ['a'])
