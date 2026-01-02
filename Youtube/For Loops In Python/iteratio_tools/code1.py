
#! iterator loops using __next__():- __nex__() and next() functio is same but next() is easy to write.

# >>> my_list=[1,2,3,4,5]
# >>> I=iter(my_list)
# >>> I
# <list_iterator object at 0x102554130>
# >>> I.__next__()
# 1
# >>> I.__next__()
# 2
# >>> I.__next__()
# 3
# >>> I.__next__()
# 4
# >>> I.__next__()
# 5
# >>> I.__next__()

my_list=[1,2,3,4,5]
i=iter(my_list)
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())


#! 2.

Dictionary={'a':1,'b':2}

I=iter(Dictionary)
print(I.__next__())
print(I.__next__())

#! 3.

r=range(0,5)

k=iter(r)
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
