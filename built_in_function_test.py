# Use map() to create a function which finds the length of each 
# word in the phrase (broken by spaces) and returns the values in a list.
# The function will have an input of a string, and output a list of integers.

s = 'How long are the words in this phrase'

def word_length(s):
    return map(len, s.split())

print word_length(s)

# Use reduce() to take a list of digits and return the number that 
# they correspond to. For example, [1, 2, 3] corresponds to 
# one-hundred-twenty-three. Do not convert the integers to strings!

def digits_to_num(digits):
    return reduce(lambda a,b: a*10+b, digits)

d = [1,2,3]
print digits_to_num(d)


# Use filter to return the words from a list of words which 
# start with a target letter.

def filter_words(word_list, letter):
    print filter(lambda word: word[0]==letter, word_list)

l = ['hello','are','cat','dog','ham','hi','go','to','heart']
filter_words(l,'h')

# Use zip() and a list comprehension to return a list of the same 
# length where each value is the two strings from L1 and L2 concatenated 
# together with connector between them.

def concatenate(L1, L2, connector):
    
    L3 = [a+connector+b for (a,b) in zip(L1,L2)]
    print L3

concatenate(['A','B','C','D'],['a','b','c','d'],'-')

# Use enumerate() and other skills to return a dictionary which has 
# the values of the list as keys and the index as the value. 
# You may assume that a value will only appear once in the given list.

def d_list_(L):
    d = {key:value for value, key in enumerate(L)}
    print d

d_list_(['a','b','c'])

# Use enumerate() and other skills from above to return the 
# count of the number of items in the list whose value equals its index.

def count_match_index(L):
    count = 0
    for index, item in enumerate(L):
        if index == item:
            count +=1
    print count

count_match_index([0,2,2,1,5,5,6,10])

#shorter way with list comprehension
def count_match_index(L):
    print len([num for count, num in enumerate(L) if num ==count])

count_match_index([0,2,2,1,5,5,6,10])





















