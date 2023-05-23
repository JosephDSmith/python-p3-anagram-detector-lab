class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, possibles):
        anagram_list = []
        for test_word in possibles:
            if all(letter in test_word for letter in self.word):
                anagram_list.append(test_word)
        return anagram_list
            
                