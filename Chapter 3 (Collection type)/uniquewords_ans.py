import string
import sys
import collections

def frequency(word):
    return word[1]

words = collections.defaultdict(int)
strip = string.whitespace+string.punctuation + string.digits + "\"'"
for filename in sys.argv[1:]:
    for line in open(filename):
        for word in line.lower().split():
            wors = word.strip(strip)
            if len(word) > 2:
                words[word] += 1

for word in sorted(words.items(), key=frequency):
    print("'{0}' occurs {1} times".format(word[0], word[1]))