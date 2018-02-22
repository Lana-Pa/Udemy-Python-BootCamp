#square numbers in range and turn into list
lst = [x**2 for x in range(0,11)]
print lst

#check for even numbers in range
l = [x for x in range(11) if x%2 ==0]
print l

# F to C temperature convert
cels = [32,15,30,18]
fahr = [((9/5)* temp + 32) for temp in cels]

print fahr

#nested list comprehension

ll = [x**2 for x in [x**2 for x in range(11)]]
print ll
