class Solution:
    """
    https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/
    """
    
    def find_indexes_of_chars(self, alphabet, word):
        """
            turn str to list
            iterate list
            get alphabet.index() for char
            append chars as str
            return converted to int appended str to int
        """
        result = ''
        for i in list(word):
            result += str(alphabet.index(i))
            
        return int(result)
        
    
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        import string 
        alphabet = list(string.ascii_lowercase)
        if (self.find_indexes_of_chars(alphabet, firstWord) + self.find_indexes_of_chars(alphabet, secondWord)) == self.find_indexes_of_chars(alphabet, targetWord):
            return True
        else:
            return False
