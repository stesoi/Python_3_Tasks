import random

articles = ("the", "a", "an")
nouns = ("cat", "dog", "man", "woman", "pig", "sun", "goat", "pen")
verbs = ("sang", "ran", "jumped", "walked", "thought", "wrote", "took", "looked", "ate")
adverbs = ("loudly", "quietly", "well", "badly", "now", "easily", "often")

for i in range(5):
    if(random.randint(0, 1) == 0):
        print(random.choice(articles), random.choice(nouns), random.choice(verbs), random.choice(adverbs))
    else:
        print(random.choice(articles), random.choice(nouns), random.choice(verbs))