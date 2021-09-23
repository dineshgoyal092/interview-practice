from collections import OrderedDict
d = {"third": 3, "first": 1, "fourth": 0, "second": 2}
s = OrderedDict(sorted(d.items(),key= lambda x : x[1]))
print s
min1 = min(d.keys(), key = lambda x: d[x])
print(min1)
s = sorted((value,key) for (key,value) in d.items())
from collections import OrderedDict
print(s)
s= dict(sorted(d.items()))
print(s)
print(s['first'])


