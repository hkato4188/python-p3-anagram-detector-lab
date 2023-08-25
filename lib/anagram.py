import ipdb

class Anagram():
    def __init__(self, word):
        self.word = word
    
    def match(self, anagram_list):    
        original_word = sorted(self.word)
        matches = []
        for possible_match in anagram_list:
            if original_word == sorted(possible_match):
                matches.append(possible_match)
        
        return matches

    


