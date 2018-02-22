#using filter with lambda to find even numbers in a list
#only for functions that return Boolean (True/False)
#the filter is filtering out everything that is not True

lst = range(20)
print filter(lambda num: num%2==0,lst)

#find numbers in a list that greater than 3

print filter(lambda num: num>3, lst)


