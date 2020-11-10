import functools

print(functools.reduce(lambda sum, word: sum + len(word), ["I", "use", "markdown", "because", "I", "don't", "know", "How", "To", "Meet", "Ladies"], 0))
