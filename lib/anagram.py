class Anagram:
    def __init__(self, word):
        self.word = word
        
    def match(self, list):
        newlist=[]
        new_word1 = [letter for letter in self.word ]
        new_word1.sort()
        for a_word in list:
            new_word2 = [letter for letter in a_word ]
            new_word2.sort()
            if new_word1 == new_word2:
               newlist.append(a_word)
        self.list=newlist
        return newlist

