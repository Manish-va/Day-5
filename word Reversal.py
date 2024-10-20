class WordReversal:  
  def __init__(self, word):  
    self.word = word  
  
  def reverse(self):  
    return self.word[::-1]  
  
word = WordReversal("hello")  
print(word.reverse()) 