# temp convert example
temps = [0,15,25,30]

t = map(lambda T: T*1.8 + 32, temps)

print t

# for python 3.0

t = list(map(lambda x: (9/5)*x + 32, temps))

#working with several lists

a = [1,2,3]
b = [4,5,6]
c = [7,8,9]

summ = map(lambda x,y,z: x+y+z, a,b,c)
print summ

