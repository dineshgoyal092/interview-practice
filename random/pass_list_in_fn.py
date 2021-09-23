def func(d=[1,2]):
    d.append(5)
    print(d)
    if 2 in d:
        d.remove(2)
    print(d)
# x = True
# print x # foo
# d = [1,2,3]
# d = [1]
func()
func([3,2])
func()
func()

# print d # foo
# func(d)
# print d

