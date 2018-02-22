#find max in sequence
mx = lambda a,b: a if (a>b) else b

#use reduce to find max in a list
ls = [47,33,22,11,78]
print reduce(mx,ls)

#use reduce to find sum of list elements
summ = lambda a,b: a+b
ls = [12,1,8,65]
print reduce(summ,ls)



