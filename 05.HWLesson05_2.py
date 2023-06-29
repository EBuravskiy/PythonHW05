print("Enter the word in small Latin letters")
word = (input())
print("Entered word:", word)
a = e = i = o = u = y = 0
vowels = 0
consonants = 0
for letter in word:
    if letter == "a":
        a += 1
        vowels += 1
    elif letter == "e":
        e += 1
        vowels += 1
    elif letter == "i":
        i += 1
        vowels += 1
    elif letter == "o":
        o += 1
        vowels += 1
    elif letter == "u":
        u += 1 
        vowels += 1
    elif letter == "y":
        y += 1
        vowels += 1
    elif letter == "-":
        sign = "-"
    else:
        consonants += 1
print ("The number of vowels in a word", vowels)
print ("The number of consonants in a word", consonants)
print ("a = ", a)
print ("e = ", e)
print ("i = ", i)
print ("o = ", o)
print ("u = ", u)
print ("y = ", y)
if a == 0 or e == 0 or i == 0 or o == 0 or u == 0 or y == 0:
    print ("False! Not all vowels are in the word")