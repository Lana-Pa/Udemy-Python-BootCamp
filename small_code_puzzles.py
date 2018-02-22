# reverse print
# s = raw_input()
#
# print s[::-1]
# print s.upper()
# print s.lower()
# print s.split("a")
# print s.count("a")

#print in one line numbers

# n = int(raw_input())
#
# print ''.join(str(x) for x in xrange(1, n + 1))

#create generator and print dictionary key-value pairs
# d = {'k1':1, 'k2':2, 'k3':3}
#
# for k,v in d.iteritems():
#     print k+':' ,v


#list comprehension

# l = []
# for letter in "word":
#     l.append(letter)
# print l

# l = [letter for letter in "word"]
# print l
#
# lst=[x**2 for x in range(1,11)]
# print lst
#
# lst2=[number for number in range(11) if number % 2 == 0]
# print lst2

#convert C to F
#
# cels = [0,14,20,25,30]
# far = [(temp*(9/5.0)+32) for temp in cels]
# print far
#
# #nested list comprehensiom
#
# lst=[x**2 for x in [x**2 for x in range(11)]]
# print lst


#using for, split() and if to create a statement tha print words that start with s
# st = 'Print only the words that start with s in this sentence'
#
# lst = st.split()
# print lst
# for i in lst:
#     if i[0]=='s':
#         print i

#Use range() to print all the even numbers from 0 to 10.
#
# r = range(0,11,2)
# print r

#Use List comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
#
# lst=[x for x in range(1,51) if x%3==0]
# print lst

#Go through the string below and if the length of a word is even print "even!"
# st = 'Print every word in this sentence that has an even number of letters'
# s = st.split()
# for i in s:
#     if len(i)%2==0:
#         print "Even!"

#  Write a program that prints the integers from 1 to 100. But for multiples of three print
# "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers
# which are multiples of both three and five print "FizzBuzz".

# for i in xrange(1,101):
#     if i%3==0:
#         print 'Fizz'
#         continue
#     if i%5==0:
#         print "Buzz"
#         continue
#     if i%3==0 and i%5==0:
#         print "FizzBuzz"
#         continue
#     print i

#Use List Comprehension to create a list of the first letters of every word in the string below:
# st = 'Create a list of the first letters of every word in this string'
#
# l = [x[0] for x in st.split()]
# print l

#check if the number is prime

# def is_prime(num):
#     for i in range(2,num):
#         if num % i==0:
#             print num, " Number is not prime"
#             break
#     else:
#         print num, "number is prime"
#
# is_prime(12)


#lambda function

# def even(num):
#     return num%2 == 0
#
# print even(4)

# even = lambda num: num%2 ==0
# print even(12)
#
# #reverse string with lambda
#
# rev = lambda st : st[::-1]
# print rev('lana')
#
# #lambda with two arguments
# adds = lambda x,y: x+y
#
# print adds(2,3)

#volume of a sphere

# from math import pi
# def vol(r):
#     return round(4.0/3.0 * pi*r**3.0,2)
#
# print vol(5)

#check whether the number is in a given range
#
# def in_range(n,x,y):
#     if n in range(x,y+1):
#         return True
#     else: return False
#
# print in_range(5,2,10)

#count number of uppercase letters and lowercase letters in a string
#
# s = "Hello, Mrs. Paulikava! How are you Today?"
#
# def count_let(s):
#     count_up = 0
#     count_lo = 0
#     st = s.replace(" ","")  # delete white space
#
#     print st
#     for i in st:
#         if i.isupper():
#             count_up +=1
#         else:
#             count_lo +=1
#     print "No of uppercase characters: ", count_up
#     print "No of lowercase characters: ", count_lo
#     print
#
#
# print count_let(s)

#function that takes a list and returns a unique elements of the first list
#
# with sets
# ls = [1,1,1,5,5,8,8,4,4,3]
# def uniq(ls):
#     st = set(ls)
#     return list(st)
#
# print "Unique list ", uniq(ls)

#just loop
# ls = [1,1,1,5,5,8,8,4,4,3]
# un_ls = []
# def uniq(ls):
#     for i in ls:
#         if i not in un_ls:
#             un_ls.append(i)
#     return un_ls
#
#
# print "Unique list ", uniq(ls)



#convert list to tuple and print hash of tuple
# n = int(raw_input())
# integer_list = map(int, raw_input().split())
# t = tuple(integer_list)
# print hash(t)


#
# x = int(raw_input())
# y = int(raw_input())
# z = int(raw_input())
# n = int(raw_input())
#
# print [[i,j,k] for i in xrange(x+1) for j in xrange(y+1) for k in xrange(z+1) if (i+j+k)!= n]


# add a phone number to contacts and print in lines

# contacts = {}
# n = 2
# for i in range(n):
#     name = raw_input('Enter name:')
#     phone = raw_input('Enter phone: ')
#     contacts[name] = phone
#
# for i,j in contacts.items():
#     print i, j

#multiply all items in a list

# int_list = map(int, raw_input().split())
#
# def multiply(int_list):
#     prod = 1
#     for i in int_list:
#         prod = prod * i
#     return prod
#
# print multiply(int_list)

#check whether a passed string is palindrome or not
# st = raw_input()
# s = st.replace(" ","")  # delete white spaces
# print s
#
# def palindrome(s):
#     rev_st = s[::-1]
#     if s == rev_st:
#         return True
#     else: return False
#
# print palindrome(s)

#check whether a string is pangram or not (has all alphabet letters)
# import string
#
# st = 'lana'
#
# def ispangram(st, alphabet = string.ascii_lowercase):
#     count = 0
#     for i in alphabet:
#         if i not in st:
#             print "Not pangram"
#             break
#         else:
#             count+=1
#         if count == len(alphabet):
#             print "String is pangram"
#
# ispangram(st)

#better way
# import string
#
# def ispangram(str1, alphabet=string.ascii_lowercase):
#     alphaset = set(alphabet)
#     strset = set(str1)
#     print alphaset
#     print strset
#     if alphaset <= set(str1.lower()):
#         print "String is pangram"
#     else:
#         print "String is not pangram"
#
# ispangram("lazy dog")

# arr = [1,5,6,7,67,45]
# k = 0
# def findNumber(arr, k):
#     if k in arr:
#         print "Yes"
#     else:
#         print "Not"
#
# findNumber(arr,k)

# l=5
# r=25
#
#
# def  oddNumbers(l, r):
#     for i in range(l,r+1):
#         if i%2 !=0:
#             print i
#
#
# oddNumbers(l,r)



# Write a program that adds two numbers prints the sum to STDOUT.
# Read the input from STDIN. The first line of your input will
# contain an integer (N) that tells you how many more lines there
# are in the input. Each of the subsequent N lines contain 2 integers).
# You need to print the sum of each pair on a separate line of STDOUT.

# n = int(raw_input())
# for i in range(n):
#     a, b = raw_input().split()
#     print int(a) + int(b)


# Given a string, return a new string where the first and last chars have been exchanged.

# def front_back(str):
#     if len(str)>1:
#         str2 = str[-1]+str[1:-1]+str[0]
#         return str2
#     else:
#         return str
#
# print front_back('a')


# Given a non-empty string like "Code" return a string like "CCoCodCode".
# string_splosion('Code')  'CCoCodCode'
# string_splosion('abc')  'aababc'
# string_splosion('ab')  'aab'
#
# def string_splosion(str):
#   result = ""
#   # On each iteration, add the substring of the chars 0..i
#   for i in range(len(str)):
#     result = result + str[:i+1]
#   return result
#
# print string_splosion('Marshmello')

# Given an array of ints, return True if
# one of the first 4 elements in the array is a 9. The array length may be less than 4.

# def array_front9(nums):
#   if len(nums)>4:
#     if 9 in nums[:4]:
#       return True
#     else:
#       return False
#   if len(nums)<4:
#     if 9 in nums:
#       return True
#     else:
#       return False
#
# Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
#
# def array123(nums):
#     for i in range(len(nums) - 2):
#         if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3:
#             return True
#
#     return False

# Given 2 strings, a and b, return the number of the positions
# where they contain the same length 2 substring. So "xxcaazz" and
# "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings
# appear in the same place in both strings.

# def string_match(a, b):
#     # Figure which string is shorter.
#     shorter = min(len(a), len(b))
#     count = 0
#
#     # Loop i over every substring starting spot.
#     # Use length-1 here, so can use char str[i+1] in the loop
#     for i in range(shorter - 1):
#         a_sub = a[i:i + 2]
#         b_sub = b[i:i + 2]
#         if a_sub == b_sub:
#             count = count + 1
#
#     print count
#
# string_match('abc', 'abc')


#Count how many 'hi' in string

# str='hi hija hihhi'
# count = 0
# for i in range(len(str)-1):
#     if str[i:i+2] == 'hi':
#         count +=1
# print count

# def end_other(a, b):
#   al = a.lower()
#   bl = b.lower()
#   alen = len(a)
#   blen = len(b)
#   if alen>=blen:
#       if al[-blen:]==bl:
#         return True
#       else:
#           return False
#   elif blen >= alen:
#       if bl[-alen:] == al:
#         return True
#       else:
#         return False
#
#
# print end_other('AbC', 'HiaBc')

#
# def centered_average(nums):
#     sum = 0
#
#     nums.remove(min(nums))
#     nums.remove(max(nums))
#
#     for i in nums:
#         sum = sum + i
#
#     aver = sum / len(nums)
#     return aver
#
#
# print centered_average([1,1,-2,-2,3,4,100,100])

# Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
# def has22(nums):
#   for i in range(len(nums)-1):
#     if nums[i]==2 and nums[i+1]==2:
#       return True
#   return False

# for i in range(1,21):
#     if i%3==0:
#         print "Fizz"
#     elif i%5==0:
#         print "Buzz"
#     elif i%3==0 and i%5==0:
#         print "FizzBuzz"
#     else:
#         print i


