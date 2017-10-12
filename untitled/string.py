import collections
sentence = """As far as the laws of mathematics refer to reality they are not certain as far as they are certain they do not refer to reality"""
x = sentence.lower()
print("split check",x.split())

words = x.split()
cnt = collections.Counter(sentence.split())

print("counter object---",cnt)

word_counts = collections.Counter(words)
print("sorted word_counts-----",word_counts.items())
for word, count in sorted(word_counts.items()):
    print('"%s" -- %d time%s.' % (word, count, "s" if count > 1 else ""))

    print('"%s" --%d time%s'%(word,count,"s" if count > 1 else ""))