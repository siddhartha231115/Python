def reverse_words(s):
    words = s.split()
    return " ".join(reversed(words))
s = " best is the siddhatha"
print(reverse_words(s))