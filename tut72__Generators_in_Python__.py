"""
Iterable - __iter__() or __getitem__()
Iterator - __next__()
Iteration - jis ko aapan iterate kr skte  hia

"""

def gen(n):
    for i in range(n):
        yield i

g = gen(4)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())


# for i in (g):
#     print(i)
        


h = "Shashwat"
it = iter(h)
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
# print(it.__next__())
# for i in (h):
#     print(i)