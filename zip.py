l1 = [1,2,3,4,5]
l2 = [2,87,9,5,3]

print zip(l1,l2)

d1= {1:'a', 2:'b', 3:'c'}
d2= {4:'d', 5:'e', 6:'f'}
print d1.items()
print d2.items()
print'---------------------'
print zip(d1,d2)  #combines only keys
print zip(d1, d2.values()) # combines keys from 1 with values from 2
print '--------------------'
#switch keys and values of the two dictionaries
d3 = {}
for d1key, d2val in zip(d1, d2.values()):
    d3[d1key]= d2val

print d3

