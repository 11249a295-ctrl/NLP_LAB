
from collections import Counter

corpus = [
    [("The", "DET"), ("dog", "NOUN"), ("barks", "VERB")],
    [("A", "DET"), ("cat", "NOUN"), ("runs", "VERB")],
    [("The", "DET"), ("cat", "NOUN"), ("eats", "VERB")]
]

emission = Counter((word, tag) for sentence in corpus
                   for word, tag in sentence)

tag_count = Counter(tag for sentence in corpus
                    for word, tag in sentence)

words = input("Enter sentence: ").split()

for word in words:
    candidates = [
        (tag, emission[(word, tag)] / tag_count[tag])
        for tag in tag_count if emission[(word, tag)] > 0
    ]
    if candidates:
        tag = max(candidates, key=lambda x: x[1])[0]
    else:
        tag = "UNKNOWN"
    print(word, ":", tag)
