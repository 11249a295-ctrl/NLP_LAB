
states = ["DET", "NOUN", "VERB"]

transition = {
    "DET": {"DET": 0.1, "NOUN": 0.8, "VERB": 0.1},
    "NOUN": {"DET": 0.1, "NOUN": 0.1, "VERB": 0.8},
    "VERB": {"DET": 0.5, "NOUN": 0.3, "VERB": 0.2}
}

emission = {
    "The": {"DET": 0.9},
    "dog": {"NOUN": 0.9},
    "barks": {"VERB": 0.9}
}

words = ["The", "dog", "barks"]
V = [{}]
back = [{}]

for state in states:
    V[0][state] = 0.33 * emission[words[0]].get(state, 0)
    back[0][state] = None

for t in range(1, len(words)):
    V.append({})
    back.append({})
    for state in states:
        options = [
            (V[t-1][prev] * transition[prev][state]
             * emission[words[t]].get(state, 0), prev)
            for prev in states
        ]
        V[t][state], back[t][state] = max(options)

best = max(V[-1], key=V[-1].get)
path = [best]

for t in range(len(words)-1, 0, -1):
    path.insert(0, back[t][path[0]])

print(list(zip(words, path)))
