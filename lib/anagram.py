# your code goes here!
class Anagram:
    pass
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        return [word for word in word_list if self.is_anagram(word)]
# Example: 
# listen = Anagram("listen")
# result = listen.match(['enlists', 'google', 'inlets', 'banana'])
# print(result)

    def is_anagram(self, other_word):
        return sorted(self.word.lower()) == sorted(other_word.lower())

# Example2:
# word1 = "listen"
# word2 = "silent"
# word3 = "hello"

# result1 = is_anagram(word1, word2)
# result2 = is_anagram(word1, word3)

# print(f"{word1} and {word2} are anagrams: {result1}")
# print(f"{word1} and {word3} are anagrams: {result2}")
