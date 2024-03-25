# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, possible_anagrams):
        return [word for word in possible_anagrams if self.is_anagram(word)]

    def is_anagram(self, other_word):
        # Check if two words are anagrams
        return sorted(self.word.lower()) == sorted(other_word.lower())