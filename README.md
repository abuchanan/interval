# Interval

A small utility class for representing 0-based, half-open intervals.

# Example

```python
from interval import Interval

a = Interval(10, 20)

a.start == 10
a.end == 20
a.length == 10

10 in a
9 not in a
19 in a
20 not in a

b = Interval(10, 12)
# Implements __contains__
b in a
a not in b

c = Interval(5, 15)
a.overlaps(c)

d = Interval(5, 15)
# Implements __eq__
c == d
# and __hash__
hash(c) == hash(d)

# Implements __lt__
a < c
```


# Testing

```python setup.py nosetests```
