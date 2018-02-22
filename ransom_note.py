#ransom note

def can_construct(a,b):
    st1 = a.replace(" ","")
    st2 = b.replace(" ","")
    d1 = dict()
    d2 = dict()

    res = 0
    for letter in st1:
        if letter not in d1:
            d1[letter]=1
        else:
            d1[letter]+=1

    for letter in st2:
        if letter not in d2:
            d2[letter] = 1
        else:
            d2[letter] += 1

    for key in d1:
        if key in d2:
            if d2[key] >= d1[key]:
                res += 1

    if res == len(d1):
        return True
    else:
        return False

print can_construct("aa","aab")
