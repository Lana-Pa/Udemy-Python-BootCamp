#enumerate counts elements by returning a tuplec(count, element)
lst = ['a', 'b', 'c', 'd', 'f']

for number, item in enumerate(lst):
    print number, item
print '--------------------------'

#use it like tracker
for count, item in enumerate(lst):
    if count>=2:
        break
    else:
        print count, item

#we can change starting index
months = ['March', 'April', 'May', 'June']
print list(enumerate(months, start = 3))