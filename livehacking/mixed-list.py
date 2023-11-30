#!/usr/bin/env python

l = []

l.append(42)
l.append(42.666)
l.append(False)
l.append("abc")
l.append([1, 2, 'drei'])
l.append((1, 2, 'drei'))
l.append(set('abc'))
l.append(dict((('one', 1), ('two', 2))))

print(l)

