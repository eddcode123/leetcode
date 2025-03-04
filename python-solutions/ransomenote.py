class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Create a dictionary to count letters in magazine
        letter_count = {}
    
        # Populate the dictionary with counts from magazine
        for letter in magazine:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
        
        # Check if ransomNote can be constructed
        for letter in ransomNote:
            if letter not in letter_count or letter_count[letter] == 0:
                return False
            # Use one occurrence of the letter
            letter_count[letter] -= 1
        
        return True