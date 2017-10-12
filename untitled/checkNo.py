
''''
###reveese string

print("Enter word to reverse: ")
a = input()
print("Reverse of "+a +" is",a[::-1])

#Count Vowels

print("Enter sentences to count vowels: ")
b= input()
words = b.lower()
y=0
for x in words:
    if x in ('a','e','i','o','u'):
        y=y+1;
    else:
        continue
print("Number of vowels in the above sentences ",y)


'''
#check palindrom

"""
print("Enter word to check palindrome: ")
c= input()

word = c.lower()

if word == word[::-1]:
    print("word ",word + " is palindrome")
else:
    print("word ", word + " is not palindrome")


"""

'''
strs = "Johnny.Appleseed!is:a*good&farmer"
lis = []
for c in strs:
    if c.isalnum() or c.isspace():
        lis.append(c)
    else:
        lis.append(' ')

new_strs = "".join(lis)
print(new_strs)           #print 'Johnny Appleseed is a good farmer'
new_strs.split()         #prints ['Johnny', 'Appleseed', 'is', 'a', 'good', 'farmer']

'''

wordstring = 'it ' #was the best of times it was the worst of times '
wordstring += 'it '#was the age of wisdom it was the age of foolishness'

wordlist = wordstring.split()

print(wordlist)
counts = {}
wordfreq = []
for w in wordlist:
    if w not in wordlist:
        counts[w] = 0
    counts[w] += 1

    wordfreq.append(wordlist.count(w))


print("String\n" + wordstring +"\n")
print("List\n" + str(wordlist) + "\n")
print("Frequencies\n" + str(wordfreq) + "\n")

A0= str(zip(wordlist,wordfreq))

print("Pairs\n" + A0)

