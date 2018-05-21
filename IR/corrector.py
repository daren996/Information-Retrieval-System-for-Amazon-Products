import re
from collections import Counter
from nltk.corpus import brown
# from nltk.corpus import webtext
# from nltk.corpus import nps_chat


def word_treatment(text):
    return re.findall(r'\w+', text.lower())


# ！！这里我取用了brown语料库，如果可以的话使用文本语料库效果会更好！！
new_words = []
for w in list(brown.words()):
    new_w = word_treatment(w)
    if len(new_w) > 0:
        new_words.extend(new_w)
WORDS = Counter(new_words)


def p(word, n=sum(WORDS.values())):
    # Probability of `word`.
    return WORDS[word] / n


def correction(word):
    # Most probable spelling correction for word.
    return max(candidates(word), key=p)


def candidates(word):
    # Generate possible spelling corrections for word.
    return known([word]) or known(edits1(word)) or known(edits2(word)) or [word]


def known(words):
    # The subset of `words` that appear in the dictionary of WORDS.
    return set(w for w in words if w in WORDS)


def edits1(word):
    # All edits that are one edit away from `word`.
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)


def edits2(word):
    # All edits that are two edits away from `word`.
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))


if __name__ == '__main__':
    word1 = "korrectud"
    print(word1, correction(word1))
    word2 = "speling"
    print(word2, correction(word2))

