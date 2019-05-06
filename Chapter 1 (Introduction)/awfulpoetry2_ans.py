import random
import sys

number = 5
articles = ("the", "a", "an")
nouns = ("cat", "dog", "man", "woman", "pig", "sun", "goat", "pen")
verbs = ("sang", "ran", "jumped", "walked", "thought", "wrote", "took", "looked", "ate")
adverbs = ("loudly", "quietly", "well", "badly", "now", "easily", "often")


if(len(sys.argv) > 1):
    number = sys.argv[1]

try:
    for i in range(int(number)):
        if(random.randint(0, 1) == 0):
            print(random.choice(articles), random.choice(nouns), random.choice(verbs), random.choice(adverbs))
        else:
            print(random.choice(articles), random.choice(nouns), random.choice(verbs))
except ValueError as err:
    print(err)