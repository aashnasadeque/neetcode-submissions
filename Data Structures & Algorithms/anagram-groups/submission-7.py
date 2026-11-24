from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #1. make a list of 26 0's
        #2. for each letter in a word, add 1 to its box
        #3. turn the list to a key
        #4. add the word to that key's pile

        result = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter) - ord("a")] += 1
            result[tuple(count)].append(word)
        result = list(result.values())
        return result

        return []
        
      

            
            


        

        
            

            
            
            
           